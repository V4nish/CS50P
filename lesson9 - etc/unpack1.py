def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts                # According to Hagrid, there are 17 Sickles in a Galleon, and 29 Knuts in a Sickle, meaning there are 493 Knuts to a Galleon.

print(total(100, 50, 25), "knuts")