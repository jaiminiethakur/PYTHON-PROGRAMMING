original = (10, 20, 30, 40, 50)
deleted = ()

for i in range(len(original)):
    if i != 3:
        deleted = deleted + (original[i],)

print(deleted)