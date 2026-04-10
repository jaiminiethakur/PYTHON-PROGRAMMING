s = "PDEU College"

print(s[0:4])
print(s[5:12])
print(s[3:8])

reverse_s = ""
for char in s:
    reverse_s = char + reverse_s
print(reverse_s)