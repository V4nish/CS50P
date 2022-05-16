import re                     #  Going to be using re.sub    (for substitution - see official docs)

url = input("What is the URL of your twitter profile: ").strip()

username = re.sub("https://twitter\.com/", "", url)       # Bit of an oopsie, but it's OK...  the . means any character in regex, we'll escape it
print(f"Username: {username}")
