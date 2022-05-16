import re                                      # pip install regex

##
##  re.search is a lot more powerful and therefore, has special symbols :>
##
## . == any character except a newline
## * == 0 or more repetitions
## + == 1 or more repetitions
## ? == 0 or 1 repetitions
## {m} == m repetitions
## {m,n} == m->n repetitions
##

email = input("What's your email? ").strip()

# if re.search(".*@.*", email):                # Run, then review - What does * require - lyndon@
# if re.search("..*@..*", email):              # OK, this fixes, but not really neat, so...
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")                          