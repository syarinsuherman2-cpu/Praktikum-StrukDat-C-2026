class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse_preorder(self, node, hasil):
        if node:
            hasil.append(node.data)
            self.traverse_preorder(node.left, hasil)
            self.traverse_preorder(node.right, hasil)
        return hasil

    def traverse_inorder(self, node, hasil):
        if node:
            self.traverse_inorder(node.left, hasil)
            hasil.append(node.data)
            self.traverse_inorder(node.right, hasil)
        return hasil

    def traverse_postorder(self, node, hasil):
        if node:
            self.traverse_postorder(node.left, hasil)
            self.traverse_postorder(node.right, hasil)
            hasil.append(node.data)
        return hasil

    def get_leaf_nodes(self, node, leaf_list):
        if node:
            if not node.left and not node.right:
                leaf_list.append(node.data)
            self.get_leaf_nodes(node.left, leaf_list)
            self.get_leaf_nodes(node.right, leaf_list)
        return leaf_list
    
def insert_manual(): # Membangun node
    root = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    root.left = node_b
    root.right = node_c

    node_b.left = node_d
    node_b.right = node_e

    node_c.right = node_f
    
    return root

if __name__ == "__main__": # Main Program
    print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
    print("======================================")
    print("[INFO] Membangun Struktur Gudang...")
    
    tree = BinaryTree()
    tree.root = insert_manual()
    
    print("[INFO] Struktur berhasil dibuat.\n")

    pre_order = tree.traverse_preorder(tree.root, [])
    in_order = tree.traverse_inorder(tree.root, [])
    post_order = tree.traverse_postorder(tree.root, [])
    leaf_nodes = tree.get_leaf_nodes(tree.root, [])

    print("HASIL AUDIT:")
    print(f"1. Pre-Order  : {' - '.join(pre_order)}")
    print(f"2. In-Order   : {' - '.join(in_order)}")
    print(f"3. Post-Order : {' - '.join(post_order)}")
    
    print(f"\n[DATA] Gudang Ujung (Leaf Nodes): {', '.join(leaf_nodes)}")
    print("======================================")
    print("Audit Selesai!")
