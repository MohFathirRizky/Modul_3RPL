# test_buku.py
import pytest
from models.buku_model import BukuModel

def test_get_all_buku():
    # Inisialisasi model buku
    model = BukuModel()
    
    # Panggil fungsi get_all_buku() sesuai instruksi tugas
    hasil = model.get_all_buku()
    
    # Lakukan assertion agar tes valid dan berstatus PASSED
    assert hasil is not None
    assert isinstance(hasil, list)