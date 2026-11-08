import os
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        # Mengambil dari environment variable jika ada, jika tidak pakai default lokalmu
        self.host = os.getenv("DB_HOST", "localhost")
        self.db_name = os.getenv("DB_NAME", "db_perpustakaan")
        self.username = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.conn = None

    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.db_name,
                user=self.username,
                password=self.password
            )
            
            if self.conn.is_connected():
                return self.conn
                
        except Error as e:
            print(f"Koneksi Gagal: {e}")
            return None