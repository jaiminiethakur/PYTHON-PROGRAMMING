text = input()
vowels = 0

for char in text:
    if char in "aeiouAEIOU":
        vowels = vowels + 1

print(vowels)