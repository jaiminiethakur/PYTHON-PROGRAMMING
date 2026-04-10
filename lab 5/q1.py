import random

odd_list = []
while len(odd_list) < 5:
    num = random.randint(1, 100)
    if num % 2 != 0:
        odd_list.append(num)
print("Odd list created:", odd_list)

even_list = []
while len(even_list) < 4:
    num = random.randint(1, 100)
    if num % 2 == 0:
        even_list.append(num)
print("Even list created:", even_list)

odd_list[2] = even_list
print("List after replacing third element:", odd_list)

flat_list = []
for item in odd_list:
    if type(item) == list:
        for sub_item in item:
            flat_list.append(sub_item)
    else:
        flat_list.append(item)
print("Flattened list:", flat_list)

for i in range(len(flat_list)):
    for j in range(i + 1, len(flat_list)):
        if flat_list[i] > flat_list[j]:
            temp = flat_list[i]
            flat_list[i] = flat_list[j]
            flat_list[j] = temp
print("Sorted list:", flat_list)