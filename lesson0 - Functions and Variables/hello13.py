# Ask user for their name
name = input("What's your name: ")   

# Remove any whitespace from the input string
name = name.strip()     # Assigned from right to the left. 

# Say hello to user
print(f"Hello, {name}")   #  This is new way of formatting stuff in Python - f for format