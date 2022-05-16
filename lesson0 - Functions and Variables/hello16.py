# Ask user for their name
name = input("What's your name: ")   

# Remove any whitespace from the input string
name = name.strip().title()    # And in one line ;)

# Say hello to user
print(f"Hello, {name}")   #  This is new way of formatting stuff in Python - f for format