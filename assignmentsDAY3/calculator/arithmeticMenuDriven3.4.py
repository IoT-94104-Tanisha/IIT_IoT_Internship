def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("END")
        break

    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if choice == 1:
        print("Result of Addition:", add(a, b))

    elif choice == 2:
        print("Result of Subtraction:", subtract(a, b))

    elif choice == 3:
        print("Result of Multiplication:", multiply(a, b))

    elif choice == 4:
        print("Result of division:", divide(a, b))

    else:
        print("Invalid Choice")
