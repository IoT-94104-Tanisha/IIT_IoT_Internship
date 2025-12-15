def bill(price, tax=5):
    total = price + (price * tax / 100)
    print("Total Bill:", total)

bill(1000) #uses default tax
bill(1000, tax=10) #overrides default using keyword
