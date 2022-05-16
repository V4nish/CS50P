def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"                       # Run this  # Padma was in Ravenclaw in the books, but Gryffindor in the movies.
    print(f"{student[0]} from {student[1]}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house               

if __name__ == "__main__":
    main()
