# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for v in range(i + 1, len(nums)):
#             if nums[i] == nums[v]:
#                 return True


# def containsDuplicate(nums):
#         stack = []
#         for i in nums:
#             if i in stack:
#                 return True
#             else:
#                 stack.append(i)
#         return False

def containsDuplicate(nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

print(containsDuplicate([1,2,3,1]))


