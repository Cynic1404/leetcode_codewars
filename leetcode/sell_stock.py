# def maxProfit(prices):
#     profit = 0
#     for first in range(len(prices)):
#         for second in range(first+1, len(prices)):
#             if prices[second]-prices[first] > profit:
#                 profit = prices[second] - prices[first]
#                 print(prices[second] , prices[first],profit)
#     return profit


def maxProfit(prices):
    profit = 0
    for first in range(len(prices)-1):
        a = max(prices[first+1: len(prices)])
        if a-prices[first] > profit:
            profit = a-prices[first]
    return profit