s1 = {'Math', 'Physics', 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}

common = s1 & s2
print(common)

only_first = s1 - s2
print(only_first)

only_second = s2 - s1
print(only_second)

total_unique = s1 | s2
print(total_unique)