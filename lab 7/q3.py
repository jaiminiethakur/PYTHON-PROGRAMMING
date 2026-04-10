employees = {
    101: {"dept": "IT", "salary": 5000},
    102: {"dept": "HR", "salary": 6000},
    103: {"dept": "IT", "salary": 4000},
    104: {"dept": "HR", "salary": 7000},
    105: {"dept": "IT", "salary": 8000}
}

min_salaries = {}
max_salaries = {}

for emp in employees:
    dept = employees[emp]["dept"]
    salary = employees[emp]["salary"]
    
    if dept not in min_salaries:
        min_salaries[dept] = salary
        max_salaries[dept] = salary
    else:
        if salary < min_salaries[dept]:
            min_salaries[dept] = salary
        if salary > max_salaries[dept]:
            max_salaries[dept] = salary

print(min_salaries)
print(max_salaries)