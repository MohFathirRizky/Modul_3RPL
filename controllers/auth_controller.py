# controllers/auth_controller.py
from views.login_view import LoginView
from models.user_model import UserModel
from controllers.buku_controller import BukuController
from tkinter import messagebox

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        # Hubungkan tombol login di view ke controller
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        # Autentikasi ke database
        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo("Sukses", f"Login Berhasil sebagai {user['role']}!")
            self.view.destroy()  # Tutup jendela login
            
            # Buka halaman Buku / Dashboard Utama berdasarkan role
            self.buku_app = BukuController(user_role=user['role'])
            self.buku_app.run()
        else:
            messagebox.showerror("Error", "Username atau Password salah!")

    def run(self):
        self.view.mainloop()