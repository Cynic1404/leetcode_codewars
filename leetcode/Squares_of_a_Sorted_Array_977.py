# sort - faster O(Nlogn)
def sortedSquares(nums):
    nums = [i ** 2 for i in nums]
    nums.sort()
    return nums

# two pointers - slower O(N)
# def sortedSquares(nums):
#     left = 0
#     right = len(nums) - 1
#     res = [0] * len(nums)
#     for i in range(len(nums) - 1, -1, -1):
#         if abs(nums[left]) > abs(nums[right]):
#             res[i] = nums[left] ** 2
#             left += 1
#         else:
#             res[i] = nums[right] ** 2
#             right -= 1
#     return res

print(sortedSquares([-4,-1,0,3,10]))