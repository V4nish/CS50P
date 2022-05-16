import re    

##
##  Tighten this up even more
##
##  LYNDONW@GMAIL.COM would not work, so we need to ignore the case without changing the users input.
##

email = input("What's your email? ").strip()
       
## re.search("^[a-z0-9_\.]@(\w+\.)?\w+\.com$" - also works :O)       ::      Which you use is preference, which do you find more acceptable.
if re.search("^(\w|\.)\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):     # let's allow subdomains....    ::    ...)?  ==  one or many    ::    (\w|\.)? A word OR a full stop, ONE or MANY times
    print("Valid")
else:
    print("Invalid")   


##
## Even more magic sauce:
##
#  
# A|B      either A or B
# (...)    a group
# (?:...)  non-capturing version
#
##
    