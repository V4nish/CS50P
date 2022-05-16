import re    

##
##  Tighten this up.
##

email = input("What's your email? ").strip()
       
if re.search("^[a-zA-Z0-9_-+]+@[a-zA-Z0-9_-+]+\.com$", email):       # a-zA-Z0-9_-+  ::  then +   ::  a-zA-Z0-9_-+     ::   .com
    print("Valid")
else:
    print("Invalid")                          