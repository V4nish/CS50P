class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house.title() not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:                     # Oooh! Validate my face off!
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()