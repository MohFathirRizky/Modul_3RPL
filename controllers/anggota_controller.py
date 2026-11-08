from tkinter import messagebox

class AnggotaController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.selected_anggota_id = None

        # Muat data ke tabel saat pertama kali dibuka
        self.load_data()

        # Hubungkan tombol-tombol pada View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.add_anggota)
        self.view.btn_perbarui.configure(command=self.update_anggota)
        self.view.btn_hapus.configure(command=self.delete_anggota)

        # Event klik baris tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.get_selected_row)

    def load_data(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()
        for row in data_anggota:
            self.view.tabel.insert("", "end", values=(row["id_anggota"], row["nama"], row["alamat"]))

    def get_selected_row(self, event):
        selected_item = self.view.tabel.focus()
        if not selected_item:
            return
        
        data = self.view.tabel.item(selected_item, "values")
        if data:
            self.selected_anggota_id = data[0]
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_nama.insert(0, data[1])
            self.view.entry_alamat.delete(0, 'end')
            self.view.entry_alamat.insert(0, data[2])

    def add_anggota(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showerror("Error", "Nama dan Alamat tidak boleh kosong!")
            return

        self.model.create_anggota(nama, alamat)
        messagebox.showinfo("Sukses", "Data anggota berhasil ditambahkan!")
        self.clear_form()
        self.load_data()

    def update_anggota(self):
        if not self.selected_anggota_id:
            messagebox.showerror("Error", "Pilih data anggota yang ingin diperbarui dari tabel!")
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showerror("Error", "Nama dan Alamat tidak boleh kosong!")
            return

        self.model.update_anggota(self.selected_anggota_id, nama, alamat)
        messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
        self.clear_form()
        self.load_data()

    def delete_anggota(self):
        if not self.selected_anggota_id:
            messagebox.showerror("Error", "Pilih data anggota yang ingin dihapus dari tabel!")
            return

        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if confirm:
            try:
                self.model.delete_anggota(self.selected_anggota_id)
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.clear_form()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menghapus: {str(e)}\nPastikan relasi tabel peminjaman sudah dibersihkan.")

    def clear_form(self):
        self.selected_anggota_id = None
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')