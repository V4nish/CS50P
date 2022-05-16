import re    

##
##  More special sauce
##
## [] == set of characters
## [^] == complementing the set (cannot match any of the declared characters).
##

email = input("What's your email? ").strip()
       
if re.search("^[^@]+@[^@]+\.com$", email):       # ^ Match at the start - $ Match at the end - [^@] any character that isn't an at sign - +@ an actual @ - etc.  Remember [^] == complementing/NOT
    print("Valid")
else:
    print("Invalid")                          