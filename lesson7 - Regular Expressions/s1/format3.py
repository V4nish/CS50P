import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), (.+)$", name)   # In this instance we are using the () to *capture* each part or group of the input

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
