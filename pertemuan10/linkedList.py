class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.count == 0
    
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top   # sambung ke atas lama
        self.top = new_node        # jadi top baru
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count

    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()


# Testing
myStack = StackLinkedList()

myStack.push('https:syarin//.id')
myStack.push('https:fira//.id')
myStack.push('https:unri//.id')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())