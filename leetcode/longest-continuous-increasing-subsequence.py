def findLengthOfLCIS(nums):
    if len(nums) == 1:
        return 1
    max_len = 0
    count = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            count += 1
            max_len = max(count, max_len)
        else:
            count = 1
            max_len = max(count, max_len)
    return max_len

# extra requirement!!!!!
#the sequence should increase evenly!!!!

# def findLengthOfLCIS(nums):
#     if len(nums) == 1:
#         return 1
#     longest=0
#     temp=[]
#     diff = None
#     for i in range(1, len(nums)):
#         if not diff:
#             diff = nums[i]-nums[i-1]
#             if not diff:
#                 temp = [nums[i-1]]
#             else:
#                 temp=[nums[i-1], nums[i]]
#             longest = max(len(temp), longest)
#             continue
#         if nums[i]-nums[i-1] == diff:
#             temp.append(nums[i])
#             longest = max(len(temp), longest)
#         else:
#             diff = nums[i]-nums[i-1]
#             if not diff:
#                 temp = [nums[i-1]]
#             else:
#                 temp=[nums[i-1], nums[i]]
#             longest = max(len(temp), longest)
#             continue
#     return longest
#
# print(findLengthOfLCIS([1,3,5,4,7]))


#refactored
#
# class Solution:
#     longest = 0
#     temp = []
#     diff = None
#
#     @classmethod
#     def findLengthOfLCIS(self, nums):
#         Solution.nums = nums
#         if len(nums) == 1:
#             return 1
#         for i in range(1, len(nums)):
#             if not self.diff:
#                 self.check(index=i)
#                 continue
#             if nums[i]-nums[i-1] == self.diff:
#                 self.temp.append(nums[i])
#                 self.longest = max(len(self.temp), self.longest)
#             else:
#                 self.check(index=i)
#                 continue
#         return self.longest
#
#     @classmethod
#     def check(self, index):
#         self.diff = self.nums[index] - self.nums[index - 1]
#         if not self.diff:
#             self.temp = [self.nums[index - 1]]
#         else:
#             self.temp = [self.nums[index - 1], self.nums[index]]
#         self.longest = max(len(self.temp), self.longest)
#
#
# print(Solution.findLengthOfLCIS([2,4,6,8, 1,1,1, 2,3,4,5]))