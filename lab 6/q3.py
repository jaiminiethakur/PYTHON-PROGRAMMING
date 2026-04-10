date1 = (10, 4, 2026)
date2 = (25, 12, 2026)

months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def count_total_days(d, m, y):
    total = d
    
    for i in range(m - 1):
        total = total + months[i]
        if i == 1:
            if y % 4 == 0:
                if y % 100 != 0 or y % 400 == 0:
                    total = total + 1
                    
    for i in range(1, y):
        total = total + 365
        if i % 4 == 0:
            if i % 100 != 0 or i % 400 == 0:
                total = total + 1
                
    return total

days1 = count_total_days(date1[0], date1[1], date1[2])
days2 = count_total_days(date2[0], date2[1], date2[2])

if days1 > days2:
    diff = days1 - days2
else:
    diff = days2 - days1

print(diff)