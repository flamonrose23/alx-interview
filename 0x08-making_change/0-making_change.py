#!/usr/bin/python3
"""
Determining fewest number of coins needed
to meet given amount total
"""


def makeChange(coins, total):
    """
    Determine function related on first description
    Arguments:
    coins -- list of coin values available
    total -- the total amount to make change for
    Return:
    fewest number of coins needed, or -1 if the total cannot be met
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize DP array with 'infinity'
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make total 0
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # For each coin, update dp for every amount
        for amount in range(coin, total + 1):
            # Update by checking this coin results in fewer coins
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, total cannot be made with avail coins
    return dp[total] if dp[total] != float('inf') else -1
