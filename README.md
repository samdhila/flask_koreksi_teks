# Flask Sistem Koreksi Teks

## Deskripsi
**Sistem Koreksi Teks** adalah platform yang dirancang dengan menggunakan **Python Flask** untuk melakukan koreksi teks secara otomatis. Berdasarkan input teks yang diberikan oleh user, sistem akan mencoba memperbaiki kesalahan penulisan yang ada dalam teks. Aplikasi ini dapat digunakan untuk berbagai keperluan seperti proofreading, analisis teks, atau tugas _Natural Language Processing_ lainnya.

## Fitur
- **Visual Feedback**: Setiap tahap proses akan ditampilkan indikator untuk meningkatkan User Experience.
- **Error Highlight**: Teks yang dideteksi sebagai kesalahan akan ditandai dengan highlight warna merah untuk meningkatkan visual clarity.
- **Parallel Scrolling**: Agar bisa lebih leluasa dan efisien untuk membandingkan input text dengan corrected text.
- **Minimize Output Container**: Aplikasi berbasis web yang mudah digunakan melalui browser.

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
  git clone https://github.com/samdhila/flask-text-correction
```

Buka CMD pada directory project
```bash
  cd flask-text-correction
```

Install dependencies
```bash
  composer install
```

Update dependencies, bila diperlukan
```bash
  composer update
```

Copy **.env.example** ke **.env** di dalam root folder.
```bash
  copy .env.example .env
```

Buka file **.env** lalu ubah nama database sesuai dengan yang ada di **PhpMyAdmin**.
```bash
  DB_DATABASE=laravel
```

Generate **App Key**
```bash
  php artisan key:generate
```

Migrasikan tabel pada database
```bash
  php artisan migrate
```

Migrasikan sample data untuk tabel database
```bash
  php artisan db:seed
```

Jalankan aplikasi web Laravel
```bash
  php artisan serve
```

Buka URL localhost pada web browser
```bash
  http://127.0.0.1:8000/
```

Upload file **dummy_text.txt** untuk melakukan demo **text correction**, atau coba dummy text berikut:
```bash
  Gempa bvmi di Banda Aceh terjadi paoa sore hari kemarin
```

## Demo

Coming soon...
