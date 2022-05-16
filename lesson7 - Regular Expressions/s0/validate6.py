import re                                     

email = input("What's your email? ").strip()

if re.search(".+@.+.com", email):       # Looks good, but .com is just {any character + com}
    print("Valid")
else:
    print("Invalid")                          