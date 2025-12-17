rad = int(input("enter radius of circle: "))
l = int(input("enter length of rectangle: "))
b = int(input("enter breadth of rectangle: "))

def function1():
    import geometry
    print(f"area of circle: {geometry.area_of_circle(rad)}")

function1()

def function2():
    import geometry
    print(f"area of rectangle: {geometry.area_of_rectangle(l,b)}")

function2()