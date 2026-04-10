original = (10, 20, 30, 40, 50)
modified = ()

for i in range(len(original)):
    if i == 2:
        modified = modified + (99,)
    else:
        modified = modified + (original[i],)

print(modified)