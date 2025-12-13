def to_binary(num):
    print("Binary value:", bin(num)[2:]) #bin is built in function that gives binary string representation as 0b11000 & to exclude ob we start from 2: ...

num = int(input("Enter a number: "))
to_binary(num)