def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")      # Unwrapping the tuple using indexes.  Tuples are immutable - the values cannot be changed :)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house               

if __name__ == "__main__":
    main()
