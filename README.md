# 📚 Sistem Manajemen Perpustakaan (MVC Python & CustomTkinter)

Aplikasi Desktop Manajemen Perpustakaan berbasis Python yang dibangun menggunakan arsitektur **Model-View-Controller (MVC)**, memanfaatkan database MySQL, antarmuka grafis **CustomTkinter**, serta dilengkapi fitur autentikasi SHA-256 dan kontrol akses berbasis *role* (Admin & Mahasiswa/Anggota).

---

## 🗂️ Struktur Direktori MVC
```text
Modul_3RPL/
│
├── config/             # Konfigurasi koneksi database MySQL
├── controllers/        # Logika alur aplikasi (Auth, Buku, Anggota)
├── models/             # Interaksi database & logika bisnis (User, Buku)
├── views/              # Antarmuka pengguna (LoginView, BukuView, dll)
├── tests/              # Unit testing menggunakan Pytest
├── .github/workflows/  # Konfigurasi CI Pipeline (GitHub Actions)
├── .gitignore          # Pengaturan file/folder yang diabaikan Git
├── requirements.txt    # Daftar pustaka / dependencies Python
└── main.py             # Titik masuk utama aplikasi (Entry Point)