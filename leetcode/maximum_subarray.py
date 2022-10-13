
def maxSubArray(nums):
    res = nums[0]

    total = 0
    for n in nums:
        total += n
        res = max(res, total)
        if total < 0:
            total = 0
    return res


def maxSubArray2(nums):
    max_sum = cur_sum = nums[0]
    for i in nums[1:]:
        cur_sum = max(cur_sum+i, i)
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1,2,-1,3,4,10,10,-10,-1]))
print(maxSubArray2([1,2,-1,3,4,10,10,-10,-1]))
print(maxSubArray([]))
print(maxSubArray2([]))


