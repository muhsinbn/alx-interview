#!/usr/bin/python3
""" Making change."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Parameters:
    coins (list): A list of integers representing the values of the coins
    in your possession.
    total (int): The total amount you want to achieve with the fewest number
    of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0, returns 0.
         If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
