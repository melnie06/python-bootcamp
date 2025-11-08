grades = [85, 72, 49, 90, 66, 59]
passing = 0

for grade in grades:
    if grade >= 60:
        passing += 1

print("Passing:", passing)