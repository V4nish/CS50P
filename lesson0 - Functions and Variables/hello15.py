# Ask user for their name
name = input("What's your name: ")   

# Remove any whitespace from the input string
name = name.strip()     # Strips whitespace from left and right hand sides.


# Use another string function
name = name.title()    # Prettier

# Say hello to user
print(f"Hello, {name}")   #  This is new way of formatting stuff in Python - f for format