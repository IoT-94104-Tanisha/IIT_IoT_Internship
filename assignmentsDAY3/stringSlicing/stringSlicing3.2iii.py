text = input("Enter a string: ")

print("Uppercase first half:", text[:len(text)//2].upper())
print("Lowercase second half:", text[len(text)//2:].lower())

print("first three char are alphabets or not", text[:3].isalpha())

print("Count of 'a' in first half:", text[:len(text)//2].count('a'))
