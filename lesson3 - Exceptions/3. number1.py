# Learn about  try  and  except
#
# So, let's convert to an int, unless something goes wrong!

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except:
    print("x is not an integer")  #  This is a catch all - not particularly useful :/
    
    #
    # Whilst catching all errors and dealing with them, we can be more specific...
    #
     
