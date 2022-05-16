hello()
name = input("What's your name? ")
hello(name)


def hello(to="World"):
    print("Hello ", to)
    
# WHY doesn't this work?  Well Python is linear and procedural in this respect, so we can't call a function that does not yet exist.
