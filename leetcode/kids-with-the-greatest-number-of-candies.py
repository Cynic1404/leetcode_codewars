def kidsWithCandies(candies, extraCandies):
    max_n = max(candies)
    checker = [True if i+extraCandies>= max_n else False for i in candies]
    print(checker)

kidsWithCandies([2,3,5,1,3], extraCandies=3)
