text = input()
length = len(text)

print(text[0])
print(text[length - 1])

if length % 2 != 0:
    middle = length // 2
    print(text[middle])