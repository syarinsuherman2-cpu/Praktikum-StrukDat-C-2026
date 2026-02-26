ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

coding_only = ukm_coding.difference(ukm_robotik)
print("Daftar seluruh mahasiswa unik:", coding_only)

total_mahasiswa = ukm_coding.union(ukm_robotik)
print("Daftar seluruh mahasiswa unik:", total_mahasiswa)

print("Apakah Andi adalah anggota ukm Robotik?", "Andi" in ukm_robotik)

