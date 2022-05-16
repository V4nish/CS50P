#  Take a step back the session 0 - student.py

class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod                                              # A class method - chicken and egg, this must come first ;) Can be called without instantiating object
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
####  EVERYTHING, EXCEPT USUAL BASIC LOGIC AND A QUERY, IS WITHIN THE CLASS
    
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()