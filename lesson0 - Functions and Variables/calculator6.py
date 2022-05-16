x = float(input("What's x? "))    # -  OK, so we need decimail points....  Change to float.
y = float(input("What's y? "))

#
# Can we manipulate the output at all??
#
# round(number[, ndigits])   # From the docs - what does this mean?
#
# in the [] brackets are optional.  , ndigits = number of digits to round to - if we want to....
#

z = round(x+y)   # Break out our thoughts, one at a time...

print(z)

# Works :)
#
# or does it....
#
# 

print(f"{z}")

#
#
#

print(f"{z:,}")    #  OK, that's cool, we can format number strings to conform with regional number formatting system