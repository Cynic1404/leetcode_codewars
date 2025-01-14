def findMaxAverage(nums, k):
    s = sum(nums[:k])
    avg = s / k
    for i in range(k, len(nums)):
        s = s + nums[i] - nums[i - k]
        avg = max(avg, s / k)
    return avg


assert findMaxAverage([1,12,-5,-6,50,3], k=4) == 12.75000
