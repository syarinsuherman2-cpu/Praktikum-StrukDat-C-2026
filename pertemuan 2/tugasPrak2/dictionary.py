# dictionary.py
data = {
    "nama": "Syarin",
    "nim": 25071101299,
    "prodi": "Informatika"
}

print(data)
print("Nama:", data["nama"])

data["kelas"] = "TI-C"
print(data)


data["umur"] = 19
print(data)

# Menghapus data
del data["kelas"]
print(data)
