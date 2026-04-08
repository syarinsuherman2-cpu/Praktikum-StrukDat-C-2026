katalog = [ 
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2}, 
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} 
    ]

daftar_merk = ("set")



class Pasien:
    jumlah = 0

    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit

        Pasien.jumlah += 1

    def get_id(self):   # Getter
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_penyakit(self):
        return self.__penyakit

    def tampilkan_info(self):  # Method tampilkan info
        print("ID      :", self.__id)
        print("Nama    :", self.__nama)
        print("Penyakit:", self.__penyakit)

    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah


class PasienPrioritas(Pasien):
    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self): # Override method
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)

        if self.prioritas == "Darurat":
            print("** Segera tangani! **")


p1 = Pasien("P001", "Andi", "Flu") # objek
p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat") # objek prioritas

p1.tampilkan_info()
print()
p2.tampilkan_info()

print("\nTotal pasien:", Pasien.hitung_pasien())