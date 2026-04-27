stack = []

stack.append('https://dina.id')
stack.append('https://fira.id')
stack.append('https://unri.id')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

is_empty = not bool(stack)
print("isEmpty: ", is_empty)

print("Size: ",len(stack))