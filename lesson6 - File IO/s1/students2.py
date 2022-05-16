students = []

with open("students.csv") as file:      
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):              # But this sorts based on the whole line :/
    print(student)