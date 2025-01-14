# sort - faster O(Nlogn)
def sortedSquares(nums):
    nums = [i ** 2 for i in nums]
    nums.sort()
    return nums

# two pointers - slower O(N)
# def sortedSquares(nums):
#     left = 0
#     right = len(nums)-1
#     res = []
#     while left<=right:
#         if nums[left]**2>nums[right]**2:
#             res.append(nums[left]**2)
#             left+=1
#         else:
#             res.append(nums[right]**2)
#             right-=1
#     return res[::-1]