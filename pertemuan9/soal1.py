class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None

class ParkirDuaArah:
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

    def tampilkan_maju(self):
        print("[Maju]")
        curr = self.head
        while curr:
            print(curr.plat)
            curr = curr.next

    def tampilkan_mundur(self):
        print("[Mundur]")

        curr = self.tail
        while curr:
            print(curr.plat)
            curr = curr.prev

parkir = ParkirDuaArah()
parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")

print()
parkir.tampilkan_maju()
print()
parkir.tampilkan_mundur()