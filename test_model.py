from models.buku_model import BukuModel
model = BukuModel()

print("=== BEFORE ===")
print(model.get_all_buku())

print("\n=== UPDATE BUKU ===")
model.update_buku(
    16,
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2024
)
print("Data berhasil diupdate!")

print("\n=== AFTER UPDATE ===")
print(model.get_all_buku())

print("\n=== DELETE BUKU ===")
model.delete_buku(16)
print("Data berhasil dihapus!")

print("\n=== AFTER DELETE ===")
print(model.get_all_buku())