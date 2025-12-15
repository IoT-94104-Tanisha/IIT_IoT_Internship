def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

base = int(input("enter base: "))
exp = int(input("enter exponent: "))
print("result:", power(base, exp))
