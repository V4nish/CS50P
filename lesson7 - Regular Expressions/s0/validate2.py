email = input("What's your email? ").strip()

username, domain = email.split("@")

# if (username) and ("." in domain):    #  IF username AND "." in DOMAIN - two sep queries - same as:
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")                    # lyndon@.com :) :(