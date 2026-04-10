text = input()
vowels = 0
consonants = 0

for char in text:
    if char in "aeiouAEIOU":
        vowels = vowels + 1
    elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        consonants = consonants + 1

print(len(text))
print(vowels)
print(consonants)