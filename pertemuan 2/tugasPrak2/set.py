# set.py
data = {"Python", "Java", "C++", "Python"}  
print("Set:", data)

data.add("Go")
print("Setelah tambah:", data)

data.remove("Java")
print("Setelah hapus:", data)

print("Jumlah isi:", len(data))

print("Isi Set:")
for item in data:
    print(item)
