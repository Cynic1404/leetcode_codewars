def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

        if min_price > prices[i]:
            min_price = prices[i]
    return max_profit



print(maxProfit([2, 100, 5, 200, 1,56, 10000]))