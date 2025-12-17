

a = int(input("enter first number: "))
b = int(input("enter second number: "))

def function1():
    import calculator
    print(f"addition: {calculator.add(a,b)}")
    print(f"subtraction: {calculator.subtract(a,b)}")
    print(f"multiplication: {calculator.multiply(a,b)}")
    print(f"division: {calculator.divide(a,b)}")

function1()