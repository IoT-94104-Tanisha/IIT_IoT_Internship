def count_vowels(text):
    vowels = "aeiouAEIOU"
    v = 0
    for ch in text:
        if ch in vowels:
            v += 1
    return v

def count_consonants(text):
    vowels = "aeiouAEIOU"
    c = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            c += 1
    return c

def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "no consonants hence no ratio"
    return vowels / consonants

text = input("Enter a string: ")

vowels = count_vowels(text)
consonants = count_consonants(text)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Ratio of vowels to consonants:", vowel_consonant_ratio(vowels, consonants))
