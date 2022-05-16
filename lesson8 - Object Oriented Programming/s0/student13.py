class Student:
    def __init__(self, name, house, patronus=None):                                                         # Third item...
        if not name:
            raise ValueError("Missing name")
        if house.title() not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:                     # Oooh! Validate my face off! - Could add try/catch :)
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):                                                                                      # Returns what is returned when the object is print()
        return f"{self.name} from {self.house}"
    
    def charm(self):                                                                                        # Method
        if self.patronus == "Stag":
            return("🦌")                                                                                    # https://emojipedia.org/
        elif self.patronus == "Otter":
            return("🦦")
        elif self.patronus == "Jack Russell terrier":
            return("🐶")
        else:                                                                                                # If no else and no match - None is returned
            return("✨")
            

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())                                                                                   # from __str__ within Student of the instance: student

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()