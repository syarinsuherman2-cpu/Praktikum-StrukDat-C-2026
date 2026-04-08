stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
]

def filter_harga(data, min_harga, max_harga):
    return (filter_harga)

def info_klinik():
    klinik = (
        "Klinik Sehat Bersama",
        "Jl. Merdeka No. 10, Pekanbaru",
        "0761-12345"
    )
    
    print("Info Klinik:")
    print("Nama   :", klinik[0])
    print("Alamat :", klinik[1])
    print("Telp   :", klinik[2])
    
def rekap_penyakit():
    penyakit_unik = {p["penyakit"] for p in pasien_hari_ini} # set
    
    print("\nJenis Penyakit Unik:", penyakit_unik)
    print("Jumlah jenis penyakit:", len(penyakit_unik))
    
    # menghitung jumlah pasien per penyakit
    rekap = {}
    for p in pasien_hari_ini:
        penyakit = p["penyakit"]
        if penyakit in rekap:
            rekap[penyakit] += 1
        else:
            rekap[penyakit] = 1
    
    print("\nRekap per penyakit:")
    for penyakit in rekap:
        print(f"{penyakit} : {rekap[penyakit]} pasien")
    
    maks = max(rekap.values()) # jumlah terbanyak
    
    terbanyak = [p for p in rekap if rekap[p] == maks] # penyakit dengan jumlah terbanyak
    
    print("\nPenyakit terbanyak:", ", ".join(terbanyak), f"({maks} pasien)")
    
info_klinik()
rekap_penyakit()