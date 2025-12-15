def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator(func, x, y):
    print("Result:", func(x, y))

calculator(add, 20, 10)
calculator(subtract, 20, 10)
