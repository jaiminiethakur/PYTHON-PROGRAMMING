words = ["apple", "banana", "cherry", "date", "elderberry"]
upper_words = []

for word in words:
    upper_word = ""
    for char in word:
        if 'a' <= char <= 'z':
            upper_word = upper_word + chr(ord(char) - 32)
        else:
            upper_word = upper_word + char
    upper_words.append(upper_word)

print(upper_words)