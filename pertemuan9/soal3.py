class NodeValet:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_giliran = None

    def tambah_petugas(self, nama):
        new_node = NodeValet(nama)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node 
            self.tail = new_node
            self.tail.next = self.head 
        
        self.current_giliran = self.head 

    def giliran_berikutnya(self, n):
        if not self.head:
            return
        
        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current_giliran.nama}") 
            self.current_giliran = self.current_giliran.next 

cll = CircularLinkedList()
cll.tambah_petugas("Andi") 
cll.tambah_petugas("Budi") 
cll.tambah_petugas("Citra") 
cll.tambah_petugas("Dewi") 

print("\n--- Antrian Giliran Petugas Valet ---")
cll.giliran_berikutnya(6) 