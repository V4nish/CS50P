import re                                     

email = input("What's your email? ").strip()

# if re.search(".+@.+\.com", email):       
if re.search(".+@.+\.com$", email):       # The $ ensures that this is at the end
    print("Valid")
else:
    print("Invalid")                          