def meow(n: int) -> str:  # Type hinting that function will return a string - None shows that it will not return anything
    return "meow\n" * n
        
number: int = int(input("Number: "))

meows: str = meow(number)
print(meows, end = "")     #  Adding the end= just to keep things neat
