def getAverages(nums, k):
    if k == 0:
        return nums
    l = len(nums)
    averages = [-1] * l
    window_size = k * 2 + 1
    if window_size > l:
        return averages

    s = sum(nums[:window_size])
    averages[k] = s // window_size
    for i in range(window_size, l):
        s = s - nums[i - window_size] + nums[i]
        averages[i - k] = s // window_size
    return averages


assert getAverages([7,4,3,9,1,8,5,2,6], 3) == [-1,-1,-1,5,4,4,-1,-1,-1]
assert getAverages([100000], 0) == [100000]
assert getAverages([8], 100000) == [-1]