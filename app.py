from flask import Flask, request, jsonify, render_template
from transformers import BertTokenizer, BertForMaskedLM
import torch
import threading

# Initialize Flask app with specified folders
app = Flask(__name__, template_folder='./views', static_folder='./static')

# Load fine-tuned IndoBERT model and tokenizer at startup
print("Loading fine-tuned IndoBERT model...")
model_path = './fine-tuned-indobert'
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForMaskedLM.from_pretrained(model_path)
print("Model loaded successfully.")

# Create a lock object for thread-safe model access
model_lock = threading.Lock()

# Define Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/full_kbbi.txt')
def kbbi():
    return app.send_static_file('full_kbbi.txt')

@app.route('/text-correction', methods=['POST'])
def text_correction():
    data = request.get_json()
    raw_text = data.get('text', '')
    
    print(f"Raw text received: {raw_text}")

    corrected_text = correct_text_with_indo_bert(raw_text)
    
    print(f"Corrected text: {corrected_text}")
    
    return jsonify({"correctedText": corrected_text})

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

# Define utility functions
def mask_tokens(inputs, tokenizer):
    """ Prepare masked tokens inputs/labels for masked language modeling """
    inputs = tokenizer(inputs, return_tensors="pt", truncation=True, max_length=512)
    labels = inputs.input_ids.detach().clone()

    # Probability matrix for MLM
    probability_matrix = torch.full(labels.shape, 0.15)
    special_tokens_mask = [
        tokenizer.get_special_tokens_mask(val, already_has_special_tokens=True) for val in labels.tolist()
    ]
    probability_matrix.masked_fill_(torch.tensor(special_tokens_mask, dtype=torch.bool), value=0.0)
    masked_indices = torch.bernoulli(probability_matrix).bool()
    labels[~masked_indices] = -100  # Only compute loss on masked tokens

    inputs.input_ids[masked_indices] = tokenizer.convert_tokens_to_ids(tokenizer.mask_token)

    return inputs, labels

def correct_text_with_indo_bert(text):
    max_length = 512
    tokens = tokenizer.tokenize(text)
    chunks = [" ".join(tokens[i:i + max_length]) for i in range(0, len(tokens), max_length)]
    corrected_text_chunks = []

    for chunk in chunks:
        inputs, labels = mask_tokens(chunk, tokenizer)

        with model_lock:
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits

            predictions = torch.argmax(logits, dim=-1)
            corrected_tokens = []
            for inp, pred, label in zip(inputs.input_ids[0], predictions[0], labels[0]):
                if label != -100:
                    corrected_tokens.append(tokenizer.decode([pred], skip_special_tokens=True))
                else:
                    corrected_tokens.append(tokenizer.decode([inp], skip_special_tokens=True))

            corrected_text_chunk = " ".join(corrected_tokens).replace(" ##", "").replace("[CLS]", "").replace("[SEP]", "").replace("[PAD]", "")
            corrected_text_chunks.append(corrected_text_chunk)

    corrected_text = " ".join(corrected_text_chunks)
    return corrected_text

# Main block to ensure the model is loaded before starting the server
if __name__ == '__main__':
    try:
        print("Ensuring model is loaded...")
        test_input = "test"
        correct_text_with_indo_bert(test_input)
        print("Model is ready, starting the server...")
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)
    
    app.run(port=5000, debug=True)
