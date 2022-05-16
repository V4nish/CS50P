x = int(input("What's x? "))       # Will store an int not a string

print(f"x is {x}")

# What will go wrong?
#
# Try entering: cat
# This is NOT a syntax error, but a ValueError (written for experienced programmers - not beginner friendly too much!)
# 
# We need to enter an *integer*, so how do we account for users entering a real or float, so how can we handle these unexpected errors?
#