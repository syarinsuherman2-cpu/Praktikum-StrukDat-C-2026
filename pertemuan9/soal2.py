class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None

class SistemHapusParkir:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def hapus_kendaraan(self, plat):
        curr = self.head
        while curr:
            if curr.plat == plat:
                if curr.prev:
                    curr.prev.next = curr.next
                else: 
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else: 
                    self.tail = curr.prev
                return
            curr = curr.next

    def tampilkan_maju(self):
        curr = self.head
        while curr:
            print(curr.plat)
            curr = curr.next

sistem = SistemHapusParkir()
sistem.tambah_kendaraan("B 1111 AA")
sistem.tambah_kendaraan("D 2222 BB")
sistem.tambah_kendaraan("A 3333 CC")
sistem.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
sistem.tampilkan_maju()

sistem.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
sistem.tampilkan_maju()