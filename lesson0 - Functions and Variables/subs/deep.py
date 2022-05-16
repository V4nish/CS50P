import sys

# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 
# or (case-insensitively) forty-two or forty two. 
# 
# Otherwise output No.

# First parameter to the answer
input1 = sys.argv[1]

input1 = input1.replace(" ", "-")

if input1 == "42" or input1 == "forty-two":
    print ("Yes")