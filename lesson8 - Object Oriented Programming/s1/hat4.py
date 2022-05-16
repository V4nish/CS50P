import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod                          #  Doesn't pass in self
    def sort(cls, name):
        print(name,"is in", random.choice(cls.houses))      # Now a class variable (cls.variable)
    
Hat.sort("Harry")     # Not instantiating, just accessing a class method within the class.

# This is an oversimplified solution for the purposes of teaching the method