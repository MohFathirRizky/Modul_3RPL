# views/buku_view.py
import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("950x500")
        self.config(bg="#f0f0f0")

        # ================= FRAME KIRI: FORM INPUT =================
        self.frame_kiri = ctk.CTkFrame(self, fg_color="#ffffff", width=300)
        self.frame_kiri.pack(side="left", fill="y", padx=20, pady=20)

        ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold"), text_color="#000000").pack(pady=15)

        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku", width=240)
        self.entry_judul.pack(pady=10, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis", width=240)
        self.entry_penulis.pack(pady=10, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)", width=240)
        self.entry_tahun.pack(pady=10, padx=15, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", hover_color="darkgreen", width=240)
        self.btn_simpan.pack(pady=(20, 5), padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue", hover_color="darkblue", width=240)
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red", hover_color="darkred", width=240)
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # ================= FRAME KANAN: TABEL / DAFTAR BUKU =================
        self.frame_kanan = ctk.CTkFrame(self, fg_color="#ffffff")
        self.frame_kanan.pack(side="right", fill="both", expand=True, padx=(0, 20), pady=20)

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold"), text_color="#000000").pack(pady=15)

        # Container untuk Tabel dan Scrollbar
        table_frame = ctk.CTkFrame(self.frame_kanan, fg_color="#ffffff")
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Membuat Scrollbar
        tree_scroll = ttk.Scrollbar(table_frame)
        tree_scroll.pack(side="right", fill="y")

        # Inisialisasi ttk.Treeview untuk Tabel Data Buku
        self.tabel_buku = ttk.Treeview(
            table_frame, 
            columns=("id", "judul", "penulis", "tahun"), 
            show="headings", 
            yscrollcommand=tree_scroll.set
        )
        tree_scroll.config(command=self.tabel_buku.yview)

        # Mengatur Judul Kolom (Heading)
        self.tabel_buku.heading("id", text="ID")
        self.tabel_buku.heading("judul", text="Judul Buku")
        self.tabel_buku.heading("penulis", text="Penulis")
        self.tabel_buku.heading("tahun", text="Tahun")

        # Mengatur Lebar Kolom
        self.tabel_buku.column("id", width=50, anchor="center")
        self.tabel_buku.column("judul", width=220, anchor="w")
        self.tabel_buku.column("penulis", width=150, anchor="w")
        self.tabel_buku.column("tahun", width=70, anchor="center")

        self.tabel_buku.pack(fill="both", expand=True)