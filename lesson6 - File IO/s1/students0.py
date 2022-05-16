with open("students.csv") as file:      # 'r' as default - Read-only
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")