import re                                      # pip install regex

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")                           # @ sign alone is valid :~