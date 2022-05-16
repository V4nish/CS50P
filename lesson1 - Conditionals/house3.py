name = input("What's your name? ")       # Refactor

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                          # Catch all    
        print("Who?")