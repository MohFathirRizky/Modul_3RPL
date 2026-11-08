# models/buku_model.py
from config.database import Database

class BukuModel:
    def __init__(self):
        db = Database()
        self.connection = db.get_connection()

    def get_all_buku(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku")
        result = cursor.fetchall()
        cursor.close()
        return result

    def create_buku(self, judul, penulis, tahun):
        cursor = self.connection.cursor()
        query = "INSERT INTO buku (judul, penulis, tahun) VALUES (%s, %s, %s)"
        cursor.execute(query, (judul, penulis, tahun))
        self.connection.commit()
        cursor.close()

    def update_buku(self, id_buku, judul, penulis, tahun):
        cursor = self.connection.cursor()
        query = "UPDATE buku SET judul = %s, penulis = %s, tahun = %s WHERE id_buku = %s"
        cursor.execute(query, (judul, penulis, tahun, id_buku))
        self.connection.commit()
        cursor.close()

    def delete_buku(self, id_buku):
        cursor = self.connection.cursor()
        query = "DELETE FROM buku WHERE id_buku = %s"
        cursor.execute(query, (id_buku,))
        self.connection.commit()
        cursor.close()