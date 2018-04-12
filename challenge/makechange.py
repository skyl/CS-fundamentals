"""
Given an amount and a coin system, return the change with the fewest possible
coins.
"""

from collections import defaultdict


def getcoin(amt, coin_system):
    # return the largest coin that is less than or equal the amount
    return max(filter(lambda x: x <= amt, coin_system))


def makechange(amt, coin_system=[1, 5, 10, 25, 100]):
    change = defaultdict(lambda: 0)

    while amt > 0:
        coin = getcoin(amt, coin_system)
        change[coin] += 1
        amt -= coin

    return change
