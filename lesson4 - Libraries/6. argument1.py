import sys

try:
    print("Hello, My name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
# 
# sys.argv[0] would return the name of the python script!
# Run from command line/terminal with an argument
#
