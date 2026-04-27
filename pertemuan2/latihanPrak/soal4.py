# Data awal
nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

# 1. Tambahkan siswa baru
nilai_siswa["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90
}

# 2. Hitung nilai akhir
print("Nilai Akhir Siswa:")
for kode, data in nilai_siswa.items():
    nilai_akhir = (0.2 * data["tugas"]) + (0.3 * data["uts"]) + (0.5 * data["uas"])
    print(f"{data['nama']} = {round(nilai_akhir, 2)}")

# 3. Tampilkan siswa dengan UAS > 80
print("\nSiswa dengan nilai UAS > 80:")
for data in nilai_siswa.values():
    if data["uas"] > 80:
        print(data["nama"])