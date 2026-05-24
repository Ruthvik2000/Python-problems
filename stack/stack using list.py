stack=[]
def push():
    elements=input("enter the elements:")
    stack.append(elements)
    print(stack)
def pop_elements():
    if not stack:#condition for empty stack (or) len(stack)==0
        print("empty stack")
    else:
        stack.pop()
while True:
    