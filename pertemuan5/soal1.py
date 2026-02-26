stok_barang = [15, 40, 30, 10, 25] 

stok_barang[3]= 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse=True)
print(stok_barang)

jumlah = sum(stok_barang)
print(jumlah)

print("stok aman") if (sum(stok_barang) / len(stok_barang)) > 20 else print("waspada")