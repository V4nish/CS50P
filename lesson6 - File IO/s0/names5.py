name = input("What's your name? ")

file = open("names.txt", "a")    # a creates a new file if it doesn't exist only
file.write(f"{name}\n")          # write takes you literally - no auto new line!
file.close
