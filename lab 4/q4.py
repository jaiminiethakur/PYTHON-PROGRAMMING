num = int(input())

is_prime = True
if num < 2:
    is_prime = False
for i in range(2, num):
    if num % i == 0:
        is_prime = False

sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors = sum_divisors + i
is_perfect = (sum_divisors == num)

temp = num
digits_count = 0
while temp > 0:
    digits_count = digits_count + 1
    temp = temp // 10

temp = num
armstrong_sum = 0
while temp > 0:
    rem = temp % 10
    armstrong_sum = armstrong_sum + (rem ** digits_count)
    temp = temp // 10
is_armstrong = (armstrong_sum == num)

temp = num
reverse_num = 0
while temp > 0:
    reverse_num = (reverse_num * 10) + (temp % 10)
    temp = temp // 10
is_palindrome = (reverse_num == num)

square = num * num
temp = num
is_automorphic = True
while temp > 0:
    if temp % 10 != square % 10:
        is_automorphic = False
    temp = temp // 10
    square = square // 10

print(is_prime)
print(is_perfect)
print(is_armstrong)
print(is_palindrome)
print(is_automorphic)