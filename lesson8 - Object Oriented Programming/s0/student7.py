def main():
    student = get_student()                
    print(f"{student['name']} from {student['house']}")      # Looks good, but remember to use single quotes inside double quotes.....

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    ## or consider name = input.... return{"name": name, "house": house}

if __name__ == "__main__":
    main()
