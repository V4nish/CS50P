with open("names.txt", "r") as file:
    lines = file.readlines()           # Reading all lines, and storing them in the list 'lines'

for line in lines:
    print("hello, ", line)