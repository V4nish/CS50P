import re                     #  Make some final improvements - re.search!

url = input("What is the URL of your twitter profile: ").strip()

matches = re.search("^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)      #  OK, still ignoring parameter passing

if matches:
    print(f"Username: ", matches.group(2))     # Second group - 1st contains www. or None if not specified
