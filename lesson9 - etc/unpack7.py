def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}


print(total(**coins), "knuts")                                                         # Boom! Double asterisk does it!  Number of items in dict must match what the function expects (i.e. 3)
# print(total(galleons = 100, sickles = 50, knuts = 25), "knuts")                      # The line above is essentially this