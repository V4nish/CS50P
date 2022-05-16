class Student:                                                      # Create/Define a class - a blueprint or mould
    ...                                                             # Enough code to create a class!


def main():
    student = get_student()              
    print(f"{student.name} from {student.house}")      

def get_student():
    student = Student()                                             # New instance of Student
    student.name = input("What's your name? ").strip()              # Instance variable
    student.house = input("What house are you in? ").strip()
    return student                                                  # Returns the specific instance (student) of the class Student


if __name__ == "__main__":
    main()
