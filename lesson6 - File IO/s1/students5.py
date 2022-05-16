#  How do we sort on dicts?
students = []

with open("students.csv") as file:      
    for line in file:
        name, house = line.rstrip().split(",")
        
        student = {"name": name, "house": house}     # from the split.
        students.append(student)


def get_name(student):           # For the sorted command below
    return(student["name"])

def get_house(student):
    return(student["house"])


for student in sorted(students, key=get_name, reverse=True):  # Not actually calling the function, sorted does, hence no ()
    print(f"{student['name']} is in {student['house']}.")    