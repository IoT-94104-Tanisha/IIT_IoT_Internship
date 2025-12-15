def add(a, b):
    return a + b

def operate(func, x, y):
    result = func(x, y)
    print("Result:", result)

operate(add, 10, 5)
