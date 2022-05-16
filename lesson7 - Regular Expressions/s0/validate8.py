import re    

##
##  More special sauce
##
## ^ == matches the start of a string
## $ == matches the end of the string or just before the newline at the end of the string.
##

email = input("What's your email? ").strip()
       
if re.search("^.+@.+\.com$", email):       # Now looking for an exact match, well with a dot com anyway.  Oh and multiple @'s :%
    print("Valid")
else:
    print("Invalid")                          