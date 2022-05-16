import csv

students = []

with open("students4.csv") as file:                                          # Note new filename - extra column added, but doesn't break the code, so future proof should a new row be added                
    reader = csv.DictReader(file)                       
    for row in reader:                                    
        students.append({"name": row["name"], "home": row["home"]})   

for student in sorted(students, key=lambda student: student["name"]):    
    print(f"{student['name']} is from {student['home']}.")    