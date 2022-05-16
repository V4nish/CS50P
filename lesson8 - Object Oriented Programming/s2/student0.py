#  Take a step back the session 0 - student.py

class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    print(student)

def get_student():                                             # Why is this here?  Shouldn't everything be organised in the Student class?  This is a design principle, but also ease of coding.
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()