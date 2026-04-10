import random

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 50))

print(numbers)
search_num = int(input("Enter a number to search: "))

for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(i)