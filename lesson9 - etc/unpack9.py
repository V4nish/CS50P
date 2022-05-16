def f(*args, **kwargs):               # Takes a variable number of positional arguments and keyword arguments
    print("Positional: ", kwargs)
    
    
f(galleons = 100, sickles = 50, knuts = 25)