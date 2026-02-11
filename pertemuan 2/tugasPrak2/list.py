# list.py

data = ["Anggur", "Apel", "Pir"]
print("List:", data)

print("Item pertama:", data[0])

data.append("Go")
print("Setelah tambah:", data)

# 4. Mengubah Data
data[1] = "Apel Merah"
print("Setelah diubah:", data)

data.remove("Pir")
print("Setelah hapus:", data)

print("Jumlah isi:", len(data))

print("Isi List:")
for item in data:
    print(item)
