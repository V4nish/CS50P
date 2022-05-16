class Wizard:                                           # Name is the commonality  -  also the PARENT
    def __init__(self, name):                           # Let's keep this simple, both students and professors are wizards, so how can we make them inherit their commonalities?
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        
    
class Student(Wizard):                                  #  THIS is the CHILD, it inherits from its parents
    def __init__(self, name, house):
        super().__init__(name)                          #  Here we import from the PARENT
        self.house = house
    
        ...         # Form room, head of house, 
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
        ...         # Subject, Study room number
        
        
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Potions")

print(wizard.name)
print(student.house)
print(professor.name)
