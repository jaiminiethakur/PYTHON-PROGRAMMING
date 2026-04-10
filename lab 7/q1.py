dict1 = {"A": 10, "B": 20}
dict2 = {"C": 30, "D": 40}
dict3 = {"E": 50, "F": 60}
dict4 = {}

for key in dict1:
    dict4[key] = dict1[key]

for key in dict2:
    dict4[key] = dict2[key]

for key in dict3:
    dict4[key] = dict3[key]

print(dict4)