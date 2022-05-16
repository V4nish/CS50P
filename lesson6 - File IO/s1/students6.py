#  How do we sort on dicts?
students = []

with open("students.csv") as file:      
    for line in file:
        name, house = line.rstrip().split(",")
        
        student = {"name": name, "house": house}     # from the split.
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):    # lambda = Anonymous function: where you want to pass to another function
    print(f"{student['name']} is in {student['house']}.")    