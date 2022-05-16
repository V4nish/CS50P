name = input("What's your name? ")

with open("names.txt", "a") as file:   
    file.write(f"{name}\n")      

## No need to close, auto closes on the end of the indent:)
