import csv

students = []

with open("students3.csv") as file:                       ## Now contains headers
    reader = csv.DictReader(file)                         ## Changed from csv.reader
    for row in reader:                                    ## Revert to row  
        students.append({"name": row["name"], "home": row["home"]})   ## State name of row

for student in sorted(students, key=lambda student: student["name"]):    
    print(f"{student['name']} is from {student['home']}.")    