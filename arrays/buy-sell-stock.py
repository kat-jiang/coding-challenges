# import testmod for testing our function
from doctest import testmod
from typing import List

def max_profit(prices: List[int]) -> int:
    """You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    >>> max_profit([7,1,5,3,6,4])
    5
    >>> max_profit([7,6,4,3,1])
    0
    """

    max_profit = 0
    min_buy = prices[0]
    for i in range(1, len(prices)):
        min_buy = min(min_buy, prices[i])
        max_profit = max(max_profit, prices[i] - min_buy)
    return max_profit

# call the testmod function
if __name__ == '__main__':
    testmod(name ='max_profit', verbose = True)