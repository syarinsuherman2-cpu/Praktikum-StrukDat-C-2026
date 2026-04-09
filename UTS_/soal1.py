pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
]

#soal 1
def tampilkan_pengunjung(): #menampilkan data pengunjung
    print("===== DATA PENGUNJUNG ====")
    print("No | ID   | Nama  | Usia | Kategori | Status Kembali")
    
    for i in range(len(pengunjung_hari_ini)): #looping
        n = pengunjung_hari_ini[i]  
        status = "Kembali" if n["Sudah"] else "Belum Kembali"
        print(f"{i+1} | {n['id']} | {n['nama']} | {n['usia']} | {n['kategori']} | {status}")
        
def filter_belum_kembali(): #list pengunjung yg belum bayar
    belum = []

    for p in pengunjung_hari_ini: #loop
        if not p["kembali"]:
            belum.append(p["nama"]) #list comprehension

    belum.sort()    # sorting
    
    print("\n===== PENGUNJUNG BELUM KEMBALI =====") #menampilkan pengunjung yg belum bayar
    for i in range(len(belum)):
        print(f"{i+1}. {belum[i]}")

    print("Total belum kembali:", len(belum))

tampilkan_pengunjung() #memanggil fungsi untuk output
filter_belum_kembali()

