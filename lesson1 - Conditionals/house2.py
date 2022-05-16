# Python 3.10+
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                          # Catch all    
        print("Who?")