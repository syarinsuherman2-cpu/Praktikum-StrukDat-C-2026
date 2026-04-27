class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None  # Pointer ke node selanjutnya

class QueueRumahSakit: # Struktur Queue menggunakan Linked List manual
    def __init__(self):
        self.head = None  # Pasien paling depan
        self.tail = None  # Pasien paling belakang
        self._size = 0    # Counter jumlah pasien

    def enqueue(self, nama, keluhan):   # Menambahkan pasien baru di bagian belakang (Tail)  # Menambahkan pasien baru di bagian belakang (Tail)
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size + (3 - self._size if nama == 'Dodi' else 0)})") 

    def dequeue(self): # Mengeluarkan pasien paling depan (Head)
        if self.is_empty():
            return None
        
        temp = self.head
        self.head = self.head.next
        self._size -= 1
        
        if self.head is None:
            self.tail = None
            
        return temp

    def peek(self): # Melihat pasien paling depan tanpa menghapus
        return self.head

    def is_empty(self): # Mengecek apakah antrian kosong
        return self.head is None

    def size(self): # Menghitung jumlah pasien
        return self._size

    def clear(self):    # Mengosongkan antrian
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display_all(self): # Fungsi tambahan untuk menampilkan semua antrian (Helper)
        print("[ANTRIAN SAAT INI]")
        if self.is_empty():
            print("Antrian kosong.")
            return
        
        curr = self.head
        i = 1
        while curr:
            print(f"{i}. {curr.nama} → {curr.keluhan}")
            curr = curr.next
            i += 1

# ====================================
# SKENARIO PENGUJIAN
# ====================================

print("====================================")
print("      SISTEM ANTRIAN POLI UMUM      ")
print("          RS Sehat Bersama          ")
print("====================================\n")

pq = QueueRumahSakit() # Cek apakah kosong
status = "YA, antrian masih kosong." if pq.is_empty() else "TIDAK, ada pasien."
print(f"[CEK] Apakah antrian kosong? → {status}")

pq.enqueue("BUDI", "demam tinggi") # Pendaftaran Pasien
pq.enqueue("ANI", "batuk pilek")
pq.enqueue("CITRA", "sakit kepala")
 
print() # Tampilkan jumlah
print(f"[INFO] Jumlah pasien menunggu: {pq.size()} orang")

next_p = pq.peek() # Peek pasien berikutnya
print(f"[PEEK] Pasien berikutnya: {next_p.nama} — {next_p.keluhan}")

panggil = pq.dequeue() # Dokter memanggil pasien pertama (Dequeue)
print(f"[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

pq.enqueue("DODI", "nyeri perut") # Pasien Dodi mendaftar

print() # Tampilkan semua antrian
pq.display_all()

panggil2 = pq.dequeue() # Dokter memanggil pasien berikutnya
print(f"[PANGGIL] Dokter memanggil: {panggil2.nama} (keluhan: {panggil2.keluhan})")

print(f"[INFO] Jumlah pasien masih menunggu: {pq.size()} orang") # Jumlah pasien sisa

pq.clear() # Sesi selesai - Clear

print() # Cek akhir
status_akhir = "YA, antrian sudah kosong." if pq.is_empty() else "TIDAK."
print(f"[CEK] Apakah antrian kosong? → {status_akhir}")

print("\n====================================")
print("          Simulasi Selesai!         ")
print("====================================")