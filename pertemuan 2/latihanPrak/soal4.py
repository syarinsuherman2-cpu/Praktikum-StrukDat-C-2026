nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}

nilai_siswa["S04"] = {
    "nama": "Fafa", 
    "tugas": 85, 
    "uts": 80,
    "uas": 90
    }


print(nilai_siswa)

print("Nilai Akhir Siswa:")
for kode, data in nilai_siswa.items():
    nilai_akhir = (
        data["tugas"] * 0.2 +
        data["uts"] * 0.3 +
        data["uas"] * 0.5
    )
    print(f"{data['nama']} : {nilai_akhir:.2f}")

print("Siswa dengan nilai UAS diatas 80:")
for kode, data in nilai_siswa.items():
    if data["uas"] > 80:
        print(f"{kode} | {data['nama']} | UAS: {data['uas']}")