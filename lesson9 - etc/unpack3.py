def total(coins):
    return(coins[0] * 17 + coins[1]) * 29 + coins[2]

coins = [100, 50, 25]

print(total(coins), "knuts")