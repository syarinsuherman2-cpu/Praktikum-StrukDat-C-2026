stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
]

def filter_harga(data, min_harga, max_harga):
    return (filter_harga)

def info_klinik():
    info = ("Klinik Sehat Bersama", "Jl. Merdeka No.10", "0761-12345")
    
    print("Info Klinik:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

pasien_hari_ini = [
    {"nama": "A", "penyakit": "Flu"},
    {"nama": "B", "penyakit": "Demam"},
]

def rekap_penyakit():
    data = pasien_hari_ini

    
    # set (unik)
    unik = set([p["penyakit"] for p in data])
    print("\nJenis Penyakit Unik:", unik)
    print("Jumlah jenis penyakit:", len(unik))
    
    # frekuensi
    frek = {}
    for p in data:
        penyakit = p["penyakit"]
        frek[penyakit] = frek.get(penyakit, 0) + 1
    
    print("\nRekap per penyakit:")
    for k, v in frek.items():
        print(f"{k} : {v} pasien")
    
    # terbanyak
    maks = max(frek.values())
    hasil = [k for k in frek if frek[k] == maks]
    
    print("Penyakit terbanyak:", ", ".join(hasil), f"({maks} pasien)")

info_klinik()
rekap_penyakit()
