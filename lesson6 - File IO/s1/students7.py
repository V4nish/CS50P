# Change from storing their house to their home address
students = []

with open("students2.csv") as file:      
    for line in file:
        name, home = line.rstrip().split(",")      # ValueError?
        
        student = {"name": name, "home": home}     # from the split.
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):    # lambda = Anonymous function: where you want to pass to another function
    print(f"{student['name']} is from {student['home']}.")    