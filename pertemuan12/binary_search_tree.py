class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):  # INSERT
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return

        current = self.root
        while True:
            if id_buku < current.id:
                if current.left is None:
                    current.left = new_node
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                    return
                current = current.right

    def search(self, id_buku):     # SEARCH
        current = self.root
        while current:
            if id_buku == current.id:
                return current
            elif id_buku < current.id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, node): # INORDER TRAVERSAL
        if node:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    def traversal_inorder(self):
        self.inorder(self.root)

    def get_min(self):     # MIN
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):     # MAX
        current = self.root
        while current.right:
            current = current.right
        return current

    def height(self, node):     # HEIGHT
        if node is None:
            return -1  # sesuai contoh output (root = 0)

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'") # MAIN PROGRAM 

print("=========================================")

bst = BST()

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.traversal_inorder()

print("\n[SEARCH] Mencari ID 60...", end=" ") # SEARCH
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

min_buku = bst.get_min() # STATISTIK
max_buku = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

tinggi = bst.height(bst.root) # HEIGHT
print(f"[INFO] Tinggi (Height) Tree: {tinggi}")

print("=========================================")
print("Simulasi Selesai!")