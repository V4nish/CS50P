class Student:                                              # Made up of Classes and Methods
    def __init__(self, name, house):                        # Instance method - to initialise the content of an object from a class.   self allows the object to be manipulated
        self.name = name                                    # Instance variable
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)                         # Now passing arguments to Class so we can validate and have more control over   -   Calling Student.__init__() with name and house


if __name__ == "__main__":
    main()
