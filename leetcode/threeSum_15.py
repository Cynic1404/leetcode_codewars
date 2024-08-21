
#brute force
# def threeSum(nums):
#     res=[]
#     for f in range(len(nums)-2):
#         for s in range(f+1, len(nums) - 1):
#             if 0 - nums[f]-nums[s] in nums[s+1:]:
#                 if sorted([nums[f],nums[s], 0 - nums[f]-nums[s]]) not in res:
#                     res.append(sorted([nums[f],nums[s],0 - nums[f]-nums[s]]))
#     return res


def threeSum(nums):
    # Initialize result list to store unique triplets
    res = []

    # Sort the input list to use the two-pointer technique effectively
    nums = sorted(nums)

    # Iterate through each number in the sorted list
    for i in range(len(nums)):

        # If the current number is greater than 0, stop the loop
        # Since we can't have a positive sum with all positive numbers after this
        if nums[i] > 0:
            break

        # Skip duplicates for the current 'i' to avoid repeated triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two-pointer technique to find pairs that sum with nums[i] to zero
        left, right = i + 1, len(nums) - 1

        # While the left pointer is less than the right pointer
        while left < right:
            # Calculate the current sum of the triplet
            current_sum = nums[left] + nums[right] + nums[i]

            # If the sum is greater than zero, move the right pointer left to reduce the sum
            if current_sum > 0:
                right -= 1
            # If the sum is less than zero, move the left pointer right to increase the sum
            elif current_sum < 0:
                left += 1
            # If the sum equals zero, we've found a valid triplet
            else:
                # Append the triplet to the result list
                res.append([nums[i], nums[left], nums[right]])

                # Move both pointers inward to search for more pairs
                left += 1
                right -= 1

                # Skip duplicate values on the left side to avoid repeating the same triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    # Return the list of unique triplets
    return res


print(threeSum(nums=[-1,0,1,2,-1,-4]))