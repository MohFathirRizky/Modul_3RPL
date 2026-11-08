from config.database import Database

class AnggotaModel:
    def __init__(self):
        db = Database()
        self.connection = db.get_connection()

    def get_all_anggota(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        result = cursor.fetchall()
        cursor.close()
        return result

    def create_anggota(self, nama, alamat):
        cursor = self.connection.cursor()
        query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama, alamat))
        self.connection.commit()
        cursor.close()

    def update_anggota(self, id_anggota, nama, alamat):
        cursor = self.connection.cursor()
        query = "UPDATE anggota SET nama = %s, alamat = %s WHERE id_anggota = %s"
        cursor.execute(query, (nama, alamat, id_anggota))
        self.connection.commit()
        cursor.close()

    def delete_anggota(self, id_anggota):
        cursor = self.connection.cursor()
        query = "DELETE FROM anggota WHERE id_anggota = %s"
        cursor.execute(query, (id_anggota,))
        self.connection.commit()
        cursor.close()