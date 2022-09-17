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