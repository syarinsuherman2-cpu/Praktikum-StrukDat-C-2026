data_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def pisah_ganjil_genap(plat_array):
    ganjil = []
    genap = []

    for plat in plat_array:
        bagian = plat.split()
        nomor = bagian[1]

        angka_terakhir = int(nomor[-1])

        if angka_terakhir% 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap

data_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = pisah_ganjil_genap(data_plat)

print("plat ganjil:", ganjil)
print("plat genap:", genap)
