skema_komisi = ( 
(100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
(50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
(20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
(0,         0)   # Di bawah 20jt      -> Tidak ada komisi    
) 



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPasien:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tampilkan(self):
        print("\n===== ANTRIAN PASIEN =====")
        current = self.head
        i = 1
        
        while current:
            d = current.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['penyakit']}")
            current = current.next
            i += 1
        
        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self):
        if not self.head:
            return
        
        d = self.head.data
        print(f"Silakan masuk: {d['nama']} ({d['id']}) - {d['penyakit']}")
        self.head = self.head.next

    def cari(self, nama):
        current = self.head
        i = 1
        
        while current:
            if current.data["nama"] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['penyakit']} (posisi ke-{i})")
                return
            current = current.next
            i += 1
        
        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        current = self.head
        prev = None

        # head
        if current and current.data["id"] == id:
            print(f"{current.data['nama']} ({id}) dihapus")
            self.head = current.next
            return

        # tengah / akhir
        while current and current.data["id"] != id:
            prev = current
            current = current.next

        if not current:
            print("ID tidak ditemukan")
            return

        print(f"{current.data['nama']} ({id}) dihapus")
        prev.next = current.next

    def hitung(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count