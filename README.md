# Flask Sistem Koreksi Teks

# Table of Contents

- [Flask Sistem Koreksi Teks](#flask-sistem-koreksi-teks)
  - [Deskripsi Sistem](#deskripsi-sistem)
  - [Detail Sistem](#detail-sistem)
  - [Alur Sistem](#alur-sistem)
  - [Live Demo](#live-demo)
  - [Setup Project](#setup-project)
    - [Pre-requirements](#pre-requirements)
    - [Local Installation](#local-installation)

## Deskripsi Sistem
**Sistem Koreksi Teks** adalah platform yang dirancang dengan menggunakan **Python Flask** untuk melakukan koreksi teks secara otomatis dengan mengintegrasikan model _Machine Learning_ **IndoBERT**. Berdasarkan input teks yang diberikan oleh user, sistem akan mencoba memperbaiki kesalahan penulisan yang ada dalam teks dan menampilkan kembali hasil perbaikan teks.

## Detail Sistem
- **KBBI matching**: Sistem menggunakan pendeteksi kesalahan penulisan teks berbasis aturan/rule menggunakan pencocokan kamus KBBI.
- **REST API**: Sistem menggunakan **REST API** untuk berinteraksi antara web client dengan server Flask, untuk menerima input text user dan mengirim output text kembali.
- **Machine Learning integration**: Sistem mengintegrasikan model Machine Learning **IndoBERT** sebagai basis untuk mengoreksi kesalahan teks otomatis.
- **Visual Feedback**: Setiap tahap proses akan menampilkan indikator untuk meningkatkan User Experience.
- **Text Highlight**: Teks yang dideteksi sebagai kesalahan akan ditandai dengan highlight warna **merah**, teks yang telah dikoreksi akan ditandai dengan highlight warna **hijau** untuk meningkatkan kejelasan output.
- **Correction Statistics**: Sistem akan menampilkan statistik teks yang di-input oleh user, berapa banyak jumlah kata yang ada, berapa jumlah kata yang benar, dan berapa jumlah kata yang salah.
- **Parallel Scrolling**: Parallel Scrolling pada container - container output berfungsi agar user bisa lebih mudah untuk membandingkan input text dengan corrected text.
- **Minimize Output Container**: Minimize Output Container agar bisa menghemat space Web UI dan juga meningkatkan fokus user.
- **Copy-able Output Text**: Teks yang sudah dikoreksi bisa langsung di-copy untuk diproses/digunakan lebih lanjut.

## Alur Sistem
- **User Input Text**: User dapat mengetik input text secara manual maupun dengan mengunggah file **.txt** yang perlu dikoreksi.
- **Deteksi Kesalahan**: Sistem akan mendeteksi dan menandai kosakata yang salah berdasarkan kecocokan dengan isi kamus kosakata baku KBBI.
- **Koreksi Kesalahan**: Sistem lalu mengoreksi teks yang dianggap salah secara otomatis menggunakan model yang telah diintegrasikan.
- **Output Text**: Sistem akan menampilkan output versi teks yang sudah dikoreksi.

## Live Demo
Untuk demo percobaan aplikasi **Flask Sistem Koreksi Teks**, bisa dilakukan pada
[URL Live Demo](https://correction-samreact.zeabur.app/) ini.

Berikut ilustrasi penggunaan aplikasi:
![Demo Koreksi Teks GIF](https://github.com/samdhila/media/blob/main/flask/flask-optimized.gif)

## Setup Project

### Pre-requirements
**Python**
```bash
  https://www.python.org/downloads/
```

### Local Installation
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

Pilih sumber **download** model **IndoBERT** yang ingin digunakan pada **app.py**\
(berasal dari **HuggingFace (default)** atau **lokal**)
```bash
  # option 1 HuggingFace repository model
  model_path = 'indolem/indobert-base-uncased'
```
Link download **IndoBERT** lokal: [Google Drive](https://drive.google.com)
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
