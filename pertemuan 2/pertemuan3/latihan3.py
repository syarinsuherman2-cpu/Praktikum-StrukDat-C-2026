class MataPelajaran:
    def __init__(self, nama, jenis, kesulitan):
        self.nama = nama
        self.jenis = jenis
        self.kesulitan = kesulitan

    def mata_pelajaran(self):
        print(f"mata pelajaran ini {nama} dengan jenis {jenis}")


    def change_kesulitan (self, new_kesulitan):
        self.kesulitan = new_kesulitan

MataPelajaran1 = MataPelajaran("syarin", "mtk", "sulit")
MataPelajaran2 = MataPelajaran("cia", "kalkulus", "mudah")
MataPelajaran3 = MataPelajaran("fira", "mtk", "sedang")

MataPelajaran1.change_kesulitan("mudah banget")


