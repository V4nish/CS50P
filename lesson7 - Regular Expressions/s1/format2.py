import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), (.+)$", name)   # In this instance we are using the () to *capture* each part or group of the input

if matches:
    last = matches.group(1)                 # (0) contains metadata, so with this function we start at (1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")
