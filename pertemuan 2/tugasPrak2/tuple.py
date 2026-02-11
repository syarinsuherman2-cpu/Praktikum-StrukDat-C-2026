#tuple.py

data = ("Syarin", 19, "Informatika")
print("Tuple:", data)

print("Nama:", data[0])
print("Umur:", data[1])

print("Jumlah isi:", len(data))

print("Isi Tuple:")
for item in data:
    print(item)

# mengubah ke dalam list
data_list = list(data)
data_list[1] = 19
print("Setelah diubah:", data_list)
