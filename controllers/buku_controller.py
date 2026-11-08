# controllers/buku_controller.py
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.view = BukuView()
        self.user_role = user_role
        
        # Menyesuaikan judul jendela berdasarkan role yang login
        if self.user_role == 'admin':
            self.view.title("Sistem Manajemen Perpustakaan - Mode ADMIN")
        else:
            self.view.title("Sistem Manajemen Perpustakaan - Mode MAHASISWA")

    def run(self):
        self.view.mainloop()