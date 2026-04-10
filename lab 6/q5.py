data = ((1, 2, 3), (), (4, 5), (), (), (6,))
filtered_data = ()

for item in data:
    if len(item) > 0:
        filtered_data = filtered_data + (item,)

print(filtered_data)