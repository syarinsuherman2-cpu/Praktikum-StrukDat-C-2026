class Graph:
    def __init__(self):
        # Menyimpan adjacency list
        self.graph = {}

    # Menambahkan kota
    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    # Menambahkan jalan dua arah
    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f'[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)')

    # Menampilkan graph
    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            print(f"- {kota} terhubung ke: ", end="")

            tetangga = []

            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")

            print(", ".join(tetangga))

    # Algoritma Dijkstra
    def dijkstra(self, kota_asal):

        # Inisialisasi jarak awal
        jarak = {}

        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        # Menyimpan kota yang sudah dikunjungi
        dikunjungi = []

        while len(dikunjungi) < len(self.graph):

            # Cari kota dengan jarak terkecil
            kota_sekarang = None
            jarak_terkecil = float('inf')

            for kota in self.graph:
                if kota not in dikunjungi and jarak[kota] < jarak_terkecil:
                    jarak_terkecil = jarak[kota]
                    kota_sekarang = kota

            # Jika tidak ada kota ditemukan
            if kota_sekarang is None:
                break

            # Tandai kota sudah dikunjungi
            dikunjungi.append(kota_sekarang)

            # Update jarak tetangga
            for tetangga, bobot in self.graph[kota_sekarang]:

                jarak_baru = jarak[kota_sekarang] + bobot

                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru

        return jarak


# =========================================
# PROGRAM UTAMA
# =========================================

print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=========================================")

# Membuat object graph
g = Graph()

# Input jalan
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

# Tampilkan graph
g.tampilkan_graph()

# Jalankan Dijkstra
print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...")

hasil = g.dijkstra("Jakarta")

# Tampilkan hasil
print("\n[HASIL] Jarak Terpendek dari Jakarta:")

nomor = 1

for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {jarak} km")
        nomor += 1

print("\n=========================================")
print("Simulasi Navigasi Selesai!")