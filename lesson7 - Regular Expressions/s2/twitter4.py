import re                     #  Going to be using re.sub    (for substitution - see official docs)

url = input("What is the URL of your twitter profile: ").strip()

username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)       # Bit of an oopsie, but it's OK...  the . means any character in regex, we'll escape it.  
                                                                      # Make the s in https optional - ? (0 or 1 of the thing before).    Group the www. together.  Same with the protocol
                                                                      # These groupings () can be nested if needed
print(f"Username: {username}")
