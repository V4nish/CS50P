with open("students.csv") as file:      
    for line in file:
        name, house = line.rstrip().split(",")   # Assign two variables at once.
        print(f"{name} is in {house}")           # Much more readable