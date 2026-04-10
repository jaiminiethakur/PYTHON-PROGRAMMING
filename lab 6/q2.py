students = ((101, "Alice", 18), (102, "Bob", 19), (103, "Charlie", 18))
roll_nos = ()
names = ()
ages = ()

for student in students:
    roll_nos = roll_nos + (student[0],)
    names = names + (student[1],)
    ages = ages + (student[2],)

print(roll_nos)
print(names)
print(ages)