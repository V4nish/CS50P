students = []

with open("students2.csv") as file:      
    for line in file:
        name, home = line.rstrip().split(",")      # Number 4, Privet Drive - has a comma, the delimiter! - Change the delimiter?  But could be caught out doing that too....
        student = {"name": name, "home": home}     
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):    
    print(f"{student['name']} is from {student['home']}.")    