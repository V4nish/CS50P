# Filters out duplicate houses using loop

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()                                              # Create a set
for student in students:
    houses.add(student["house"])                            # Get rid of the if and just a small change, 

for house in sorted(houses):
    print(house)