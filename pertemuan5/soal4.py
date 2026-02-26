gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20}
]

gudang_pc[1]["kategori"] = "Aksesoris"

gudang_pc.append({"item": "Hedset", "harga": 350000, "stok":8},)
print(gudang_pc)

for x in gudang_pc:
    total = x["harga"] * x["stok"]
    print(f"item: {x["harga"]} | Total Aset: Rp{total}")