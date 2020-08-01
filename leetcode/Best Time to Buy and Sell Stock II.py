class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for first in range(len(prices)-1):
            a = max(prices[first+1: len(prices)])
            if a-prices[first] > profit:
                profit = a-prices[first]
        return profit


# def maxProfit(prices):
#     profit = 0
#     max_profit_for_day=0
#     for first in range(len(prices)):
#         for second in range(first+1, len(prices)):
#             a = prices[first]
#             b= prices[second]
#             if prices[second]-prices[first] > max_profit_for_day:
#                 max_profit_for_day = prices[second] - prices[first]
#         profit+=max_profit_for_day
#         print(profit)
# print(maxProfit([1,5,3,6,4]))