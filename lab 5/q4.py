import random

numbers = []
for i in range(30):
    numbers.append(random.randint(-50, 50))

positive_nums = []
negative_nums = []

for num in numbers:
    if num > 0:
        positive_nums.append(num)
    elif num < 0:
        negative_nums.append(num)

print(positive_nums)
print(negative_nums)