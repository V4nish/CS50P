def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"                       
    print(f"{student[0]} from {student[1]}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]                               #  Added square brackets, so now this is a mutable list, but a few more values and it gets :S - so dicts can also be used

if __name__ == "__main__":
    main()
