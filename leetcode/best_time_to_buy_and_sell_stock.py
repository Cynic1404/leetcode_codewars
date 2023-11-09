def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > profit:
            profit = prices[i] - min_price


    return profit


print(maxProfit([3,11,4,11,3,9,3,12,2,4,5]))

print(maxProfit([7,1,5,3,6,4]))


# to return day's indexes

# def maxProfit(prices):
#     if not prices or len(prices) == 1:
#         return 0, 0, 0  # No profit if only one day or empty array
#
#     min_price_idx = 0
#     max_profit = 0
#     buy_day = 0
#     sell_day = 0
#
#     for i in range(1, len(prices)):
#        if prices[i]<prices[min_price_idx]:
#            min_price_idx=i
#        else:
#             current_profit = prices[i]-prices[min_price_idx]
#             if current_profit>max_profit:
#                 max_profit=current_profit
#                 buy_day=min_price_idx
#                 sell_day=i
#
#
#     return max_profit, buy_day, sell_day

# def maxProfit(prices):
#     if len(prices) > 1:
#         res=[]
#         day_to_buy = 0
#         day_to_sell = 1
#         profit = prices[day_to_sell] - prices[day_to_buy]
#         min_price = prices[day_to_buy]
#         for i in range(1, len(prices) - 1):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#                 day_to_buy = i
#             if prices[i + 1] - prices[day_to_buy] > profit:
#                 profit = prices[i + 1] - prices[day_to_buy]
#                 day_to_sell = i + 1
#                 res.append([profit, day_to_buy, day_to_sell])
#     else:
#         return 0
#     if res:
#         print(res)
#         max=0
#         for i in res:
#             if i[0]>max:
#                 max = i[0]
#                 day_to_buy = i[1]
#                 day_to_sell = i[2]
#         return (max, day_to_buy, day_to_sell)
#     elif profit>0:
#         return (profit, day_to_buy, day_to_sell)
#     else:
#         return 0