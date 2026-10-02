MAX = 5
stack = [None] * 5
top = -1 #stack is empty

def push(book):
    global top
    if top == MAX - 1:
        print("stack is overflowed")
    else:
        top = top + 1
        stack[top] = book
        print("book is stored",book)

def pop():
    global top
    if top == -1:
        print("stack is underflow")
    else:
        book = stack[top]
        top = top - 1
        print("book arranged",book)

def peek():
    if top == -1:
        print("stack is empty")
    else:
        print("Top book:",stack[top])

def display():
    if top == -1:
        print("stack is empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])

while True:
    print("1.return book")
    print("2.Arrange book")
    print("3.Top book")
    print("4.Display")
    print("5.exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        book = input("Enter the book name: ")
        push(book)

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("program ended")
        break
    else:
        print("invalid")