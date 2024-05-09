stack=[]
for i in range(0,3):
    add=int(input("enter a number : "))
    stack.append(add)
print("added element")
print(stack)
stack.pop()
print("deleted element")
print(stack[0])
