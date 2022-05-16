import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), *(.+)$", name)   # Added * to account for 0 or many spaces

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
