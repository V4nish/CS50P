import re                     #  Make some final improvements - refactor!     :=

url = input("What is the URL of your twitter profile: ").strip()

if matches := re.search("^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):      #  OK, let's ignore the first group using (?:) instead of ()
    print(f"Username: ", matches.group(1))     # Second group - 1st contains www. or None if not specified
