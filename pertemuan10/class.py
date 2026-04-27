class StackList:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return len(self.items) == []
    pass

    def push(self, url):
        self.items.append(url)
    pass

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.items[-1]
    pass

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    pass

    def size(self):
        return (self.items)

myStacklist = StackList()

myStacklist.push("https:syarin.ac.id")
myStacklist.push("https:fira.ac.id")
myStacklist.push("https:unri.ac.id")

print("Stack: ", myStacklist.items)
print("Pop: ", myStacklist.pop())
print("Stack after Pop: ", myStacklist.items)
print("Peek: ", myStacklist.peek())
print("is_empty: ", myStacklist.is_empty())
print("Size: ", myStacklist.size())