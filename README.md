# Flask Sistem Koreksi Teks

## Deskripsi
**Sistem Koreksi Teks** adalah platform yang dirancang dengan menggunakan **Python Flask** untuk melakukan koreksi teks secara otomatis dengan mengintegrasikan model Machine Learning **IndoBERT**. Berdasarkan input teks yang diberikan oleh user, sistem akan mencoba memperbaiki kesalahan penulisan yang ada dalam teks. Aplikasi ini dapat digunakan untuk berbagai keperluan seperti proofreading, analisis teks, atau tugas _Natural Language Processing_ lainnya.

## Fitur
- **Visual Feedback**: Setiap tahap proses akan ditampilkan indikator untuk meningkatkan User Experience.
- **Text Highlight**: Teks yang dideteksi sebagai kesalahan akan ditandai dengan highlight warna merah, teks yang telah dikoreksi akan ditandai dengan highlight warna hijau untuk meningkatkan visual clarity.
- **Parallel Scrolling**: Agar bisa lebih leluasa dan efisien untuk membandingkan input text dengan corrected text.
- **Minimize Output Container**: Agar bisa menghemat space Web UI dan juga meningkatkan fokus.
- **Copy-able Output Text**: Teks yang sudah dikoreksi bisa langsung di-copy untuk digunakan lebih lanjut.

## Alur Sistem
- **User Input Text**: User dapat mengetik input text secara manual maupun dengan mengunggah file **.txt** yang akan dikoreksi.
- **Deteksi Kesalahan**: Sistem akan mendeteksi dan menandai kosakata yang salah berdasarkan kecocokan dengan isi kamus kosakata baku KBBI.
- **Koreksi Kesalahan**: Sistem lalu mengoreksi teks yang dianggap salah secara otomatis menggunakan model yang telah diintegrasikan.
- **Output Text**: Sistem akan menampilkan versi teks yang sudah dikoreksi.

![Demo Koreksi Teks GIF](https://github.com/samdhila/media/blob/main/demo_indobert.gif)

## Setup Project

### Pre-requirements

**Python**
```bash
  https://www.python.org/downloads/
```

### Installation

Clone project **Sistem Koreksi Teks**
```bash
  git clone https://github.com/samdhila/flask_koreksi_teks.git
```

Buka CMD pada directory project
```bash
  cd flask_koreksi_teks
```

Buat virtual environment
```bash
  python -m venv venv
```

Aktivasi virtual environment
```bash
  venv\Scripts\activate
```

Install requirements
```bash
  pip install -r requirements.txt
```

Install SpaCy model
```bash
  python -m spacy download en_core_web_sm
```

Pilih sumber **download** model **IndoBERT** yang ingin digunakan
(berasal dari **HuggingFace (default)** atau **lokal**) pada **app.py**
```bash
# option 1 HuggingFace repository model
model_path = 'indolem/indobert-base-uncased'
```
```bash
# option 2 local repository model
model_path = './saved_model'
```

Jalankan aplikasi web Flask
```bash
  python app.py
```

Buka URL localhost pada web browser
```bash
  http://127.0.0.1:5000/
```

Upload file **dummy_text.txt** untuk melakukan demo **text correction**, atau coba dummy text berikut:
```bash
  Gempa bvmi di Banda Aceh terjadi paoa sore hari kemarin
```

## Live Demo

**Link:** Coming soon...
