stok = [15, 50, 30, 25, 40]

stok.append(100)
stok.insert(2, 75)
stok.sort(reverse=True)

rata_rata = sum(stok) / len(stok)

print("List akhir:", stok)
print("Rata-rata:", round(rata_rata, 2))

