#!/usr/bin/env python3
"""Change comes from within"""

def makeChange(coins, total):
    """ Determines the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    numCoins = 0
    for coin in coins:
        if total <= 0:
            break
        numCoins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return numCoins
