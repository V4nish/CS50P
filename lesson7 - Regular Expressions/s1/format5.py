import re                                                  # Time to refactor!

name = input("What's your name? ").strip()
if matches := re.search("^(.+), *(.+)$", name):            # := is the walrus operator (new to python) allows you assign a value AND ask a boolean question in one
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
