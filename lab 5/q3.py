import random

numbers = []
for i in range(50):
    numbers.append(random.randint(1, 30))

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)