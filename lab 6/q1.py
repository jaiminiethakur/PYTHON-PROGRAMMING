names = ("Alice", ("Bob",), "Charlie", ("David",), "Eve", ("Frank",))
boys = 0
girls = 0

for ele in names:
    if isinstance(ele, tuple):
        boys = boys + 1
    else:
        girls = girls + 1

print(boys)
print(girls)