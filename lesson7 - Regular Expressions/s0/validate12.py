import re    

##
##  Tighten this up even more
##
##  LYNDONW@GMAIL.COM would not work, so we need to ignore the case without changing the users input.
##

email = input("What's your email? ").strip()
       
if re.search("^\w+@\w+\.com$", email, re.IGNORECASE):       # re.IGNORECASE, but still stuck with lyndon@staff.lhs.wales - only one set of \w allowed before TLD after @
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
    