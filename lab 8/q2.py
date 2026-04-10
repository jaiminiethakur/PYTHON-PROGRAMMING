day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

both_days = day1 & day2
print(both_days)

only_one_day = day1 ^ day2
print(only_one_day)

total_visitors = day1 | day2
print(total_visitors)