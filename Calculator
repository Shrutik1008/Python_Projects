def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot Divide by Zero"


def handle_input(c, x, y):
    if c == 1:
        print("Result: " + str(add(x, y)))
    elif c == 2:
        print("Result: " + str(sub(x, y)))
    elif c == 3:
        print("Result: " + str(mult(x, y)))
    elif c == 4:
        print("Result: " + str(div(x, y)))
    elif c == 5:
        print("Changing Numbers")
        assign_values()
    elif c == 6:
        print("Exiting the program...")
        quit()
    else:
        print("Invalid Choice!!!")


def assign_values():
    global a, b
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Change Numbers\n6. Exit")
    ch = int(input("Enter Your Choice: "))
    handle_input(ch, a, b)
