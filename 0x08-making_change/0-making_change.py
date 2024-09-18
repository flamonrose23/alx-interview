#!/usr/bin/python3
"""
Determining fewest number of coins needed to meet given amount total
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number decribed before
    Args:
    coins -- list of coin values available
    total -- the total amount to make change for

    Return:
    fewest number of coins needed, or -1 if the total cannot be met
    """
    if total <= 0:
        return 0

    # Initializing list to store the fewest coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
