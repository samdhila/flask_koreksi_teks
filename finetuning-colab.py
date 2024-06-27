# Install necessary libraries
!pip install transformers datasets accelerate tensorboard -U

import pandas as pd
from datasets import Dataset
from transformers import BertForMaskedLM, BertTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
import shutil
from torch.utils.tensorboard import SummaryWriter

# Load the dataset from a text file URL
data = pd.read_csv('https://raw.githubusercontent.com/samdhila/file-hosting/main/dataset_final.txt', delimiter=',', header=None)
data.columns = ['error_text', 'correct_text']

# Create a Dataset object
dataset = Dataset.from_pandas(data)

# Load IndoBERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('indolem/indobert-base-uncased')
model = BertForMaskedLM.from_pretrained('indolem/indobert-base-uncased')

# Tokenize the input text
def tokenize_function(examples):
    # Concatenate error_text and correct_text with a separator
    inputs = [text1 + tokenizer.sep_token + text2 for text1, text2 in zip(examples['error_text'], examples['correct_text'])]
    return tokenizer(inputs, padding="max_length", truncation=True, max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=True,
    mlm_probability=0.15
)

# Create a summary writer for TensorBoard
writer = SummaryWriter(log_dir='./logs')

# Define training arguments optimized for NVIDIA L4 GPU
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=3e-5,  # Adjusted learning rate
    per_device_train_batch_size=32,  # Adjusted batch size
    per_device_eval_batch_size=32,
    num_train_epochs=10,  # Increased number of epochs
    weight_decay=0.1,  # Increased weight decay
    logging_dir='./logs',  # Directory for storing logs
    logging_steps=10,  # Log every 10 steps
    save_steps=500,  # Save checkpoint every 500 steps
    save_total_limit=3,  # Limit the total number of checkpoints
    warmup_steps=1000,  # Increased number of warmup steps
    fp16=True,  # Enable mixed precision training for faster performance
    report_to="tensorboard",  # Enable logging to TensorBoard
    gradient_accumulation_steps=4  # Simulate larger batch size
)

# Add a callback to print loss during training
from transformers import TrainerCallback

class PrintLossCallback(TrainerCallback):
    def on_log(self, args, state, control, logs=None, **kwargs):
        if logs is not None:
            print(logs)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets,
    data_collator=data_collator,
    callbacks=[PrintLossCallback()]  # Add the callback here
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine-tuned-indobert')
tokenizer.save_pretrained('./fine-tuned-indobert')

# Zip the fine-tuned model
shutil.make_archive('./fine-tuned-indobert', 'zip', './fine-tuned-indobert')

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define the paths
output_zip = './fine-tuned-indobert.zip'
drive_output_dir = '/content/drive/MyDrive/fine-tuned-indobert.zip'

# Copy the zipped model to Google Drive
!cp {output_zip} {drive_output_dir}

print(f"Zipped model saved to {drive_output_dir}")

# Zip the TensorBoard logs
shutil.make_archive('./logs', 'zip', './logs')

# Copy the TensorBoard logs to Google Drive
logs_output_zip = './logs.zip'
logs_drive_output_dir = '/content/drive/MyDrive/logs.zip'

# Copy the zipped logs to Google Drive
!cp {logs_output_zip} {logs_drive_output_dir}

print(f"Zipped TensorBoard logs saved to {logs_drive_output_dir}")

# Launch TensorBoard in the background
%load_ext tensorboard
%tensorboard --logdir ./logs