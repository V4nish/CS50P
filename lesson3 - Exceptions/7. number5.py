while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")  #  This is now catches any input that isn't a number
    else:
        break
    
print(f"x is {x}")
