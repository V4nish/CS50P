class Wizard:                                           # Name is the commonality
    def __init__(self, name):                           # Let's keep this simple, both students and professors are wizards, so how can we make them inherit their commonalities?
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        
        
    
    
    
    
    
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    
class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
