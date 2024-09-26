# Flask Sistem Koreksi Teks

## Deskripsi
**Sistem Koreksi Teks** adalah platform yang dirancang dengan menggunakan **Python Flask** untuk melakukan koreksi teks secara otomatis dengan mengintegrasikan model Machine Learning **IndoBERT**. Berdasarkan input teks yang diberikan oleh user, sistem akan mencoba memperbaiki kesalahan penulisan yang ada dalam teks. Aplikasi ini dapat digunakan untuk berbagai keperluan seperti proofreading, analisis teks, atau tugas _Natural Language Processing_ lainnya.

## Fitur
- **Visual Feedback**: Setiap tahap proses akan ditampilkan indikator untuk meningkatkan User Experience.
- **Error Highlight**: Teks yang dideteksi sebagai kesalahan akan ditandai dengan highlight warna merah untuk meningkatkan visual clarity.
- **Parallel Scrolling**: Agar bisa lebih leluasa dan efisien untuk membandingkan input text dengan corrected text.
- **Minimize Output Container**: Agar bisa menghemat space Web UI dan juga meningkatkan fokus.
- **Copy-able Output Text**: Teks yang sudah dikoreksi bisa langsung di-copy untuk digunakan lebih lanjut.

## Alur Sistem
- **User Input Text**: User dapat mengetik input text secara manual maupun dengan mengunggah file **.txt** yang akan dikoreksi.
- **Koreksi Otomatis**: Sistem lalu mengoreksi kesalahan dalam teks secara otomatis menggunakan model yang telah diintegrasikan.
- **Output Text**: Sistem akan menampilkan versi teks yang sudah dikoreksi.

## Setup Project

### Pre-requirements

**Python**
```bash
  https://www.python.org/downloads/
```

### Installation

Clone project **Sistem Koreksi Teks**
```bash
  git clone https://github.com/samdhila/flask_text_correction.git
```

Buka CMD pada directory project
```bash
  cd flask_text_correction
```

Buat virtual environment
```bash
  python -m venv venv
```

Aktivasi virtual environment
```bash
  source venv/bin/activate
```

Install requirements
```bash
  pip install -r requirements.txt
```

Install SpaCy model
```bash
  pip install -r requirements.txt
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

## Demo

Coming soon...
