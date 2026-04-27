# Data tuple
barang = ("B001", "Laptop Gaming", 15000000)

# 1. Akses harga (indeks ke-2)
print("Harga barang:", barang[2])

# 2. Mencoba mengubah harga (akan error)
# barang[2] = 14000000
# ERROR karena tuple bersifat IMMUTABLE (tidak bisa diubah setelah dibuat)
# Jadi elemen di dalam tuple tidak bisa diganti seperti list

# 3. Unpacking tuple
kode, nama, harga = barang

print("Kode:", kode)
print("Nama:", nama)
print("Harga:", harga)