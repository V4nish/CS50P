name = input("What's your name? ")

# file = open("names.txt", "w")   # w is dangerous! Each time it recreates the file
file = open("names.txt", "a")    # a creates a new file if it doesn't exist only
file.write(name)
file.close

# Redo the three name thing...
