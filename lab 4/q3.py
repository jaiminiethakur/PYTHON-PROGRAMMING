text = input()
alphabets = 0
digits = 0

for char in text:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        alphabets = alphabets + 1
    elif '0' <= char <= '9':
        digits = digits + 1

print(alphabets)
print(digits)