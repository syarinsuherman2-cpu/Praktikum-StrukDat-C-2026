class Node:
  def _init_(self, data):
    self.data = data
    self.next = None


def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")


def tambahKendaraan(head, plat):
  newNode = Node(plat)

  if head is None:
    return newNode

  currentNode = head
  while currentNode.next:
    currentNode = currentNode.next

  currentNode.next = newNode
  return head


def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print("Antrian awal:")
traverseAndPrint(head)

# tambah kendaraan 
head = tambahKendaraan(head, "C 2345 KOY")

print("Setelah tambah kendaraan:")
traverseAndPrint(head)

# yg mogok
head = deleteSpecificNode(head, node3)

print("Setelah kendaraan mogok dihapus:")
traverseAndPrint(head)