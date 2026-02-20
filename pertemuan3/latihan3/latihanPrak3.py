class JadwalKuliah:
    def __init__(self, namaSiswa, jenisPelajaran, tingkatKesulitan):
        self.namaSiswa = namaSiswa
        self.jenisPelajaran = jenisPelajaran
        self.tingkatKesulitan = tingkatKesulitan

    def memperkenalkan_diri(self, namaSiswa, jenisPelajaran):
        print (f"Halo nama saya {namaSiswa} saya suka pelajaran {jenisPelajaran}")

    def change_jenisPelajaran (self, new_jenisPelajaran):
        self.jenisPelajaran = new_jenisPelajaran

mp1 = JadwalKuliah("Syarin", "Kalkulus", "Sulit")
mp2 = JadwalKuliah("Fira", "Pemograman", "Mudah")
mp3 = JadwalKuliah("Celsi", "StrukturData", "Sulit")

print(f"{mp1.namaSiswa} mengambil pelajaran {mp1.jenisPelajaran}")
mp1.change_jenisPelajaran("Algoritma Pemrograman")
print(f"{mp1.namaSiswa} mengganti pelajarannya menjadi {mp1.jenisPelajaran}")