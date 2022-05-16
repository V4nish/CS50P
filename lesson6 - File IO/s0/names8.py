with open("names.txt", "r") as file:
    lines = file.readlines()           # Reading all lines, and storing them in the list 'lines'

################################################
################################################
######        WHY YOU NO WORK!!??!!    #########
################################################
################################################

for line in lines:
    print("hello, ", line.rstrip())    # We wrote newlines when we appended, and are kind reading extra  new lines with the print command