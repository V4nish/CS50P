def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")                                               # Unpacking the list of coins to send to the function with the * prefix