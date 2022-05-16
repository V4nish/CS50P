import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), (.+)$", name)   # In this instance we are using the () to *capture* each part or group of the input

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")
