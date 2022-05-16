students = []

with open("students.csv") as file:      
    for line in file:
        name, house = line.rstrip().split(",")
        
        student = {}     # Empty dict

        student["name"] = name
        student["house"] = house

        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}.")    # Why did I just make my life/code more difficult?  
    
    # And, why single quotes inside the f string??  Already using double quotes on the print statement.