# What went wrong?

def meow(n: int):                  # Only allow an int - well, tell not demand
    for _ in range(n):
        print("meow")
        
number: int = input("Number: ")
meow(number)

####   run with mypy instead of python from the command line  --  TODO: get working easily from command line.