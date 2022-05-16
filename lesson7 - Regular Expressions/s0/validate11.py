import re    

##
##  Tighten this up more
##

email = input("What's your email? ").strip()
       
if re.search("^\w+@\w+\.com$", email):       # esp + w (\w) == word
    print("Valid")
else:
    print("Invalid")     
    
##
## More magic sauce:
##
#
# \d  Decimal digit
# \D  Not a decimal digit
# \s  Whitespace characters
# \S  Not whitespace characters
# \w  Word Character
# \W  Not a word character
#
##