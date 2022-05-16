def meow(n: int) -> str:
    """"Meow n times"""  # Triple quotes or double quotes help build docstrings
    return "meow\n" * n
        
number: int = int(input("Number: "))

meows: str = meow(number)
print(meows, end = "")
