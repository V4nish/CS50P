try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")  #  This is now catches any input that isn't a number

print(f"x is {x}")
    
# The system should now be complaining about a NameError if we enter a string.  It is outside of the scope of the: except: block where it is defined.