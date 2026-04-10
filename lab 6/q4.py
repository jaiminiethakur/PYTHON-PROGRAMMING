foods = (("Pizza", 12.5), ("Burger", 8.0), ("Pasta", 10.5))
temp_foods = ()

for item in foods:
    temp_foods = temp_foods + ((item[1], item[0]),)

sorted_temp = tuple(sorted(temp_foods, reverse=True))

final_foods = ()

for item in sorted_temp:
    final_foods = final_foods + ((item[1], item[0]),)

print(final_foods)