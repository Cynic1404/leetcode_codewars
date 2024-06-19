
def longestConsecutive(nums):
    # If the list is empty, return 0
    if not nums:
        return 0

    # Sort the list
    nums = sorted(nums)

    # Initialize the variables
    longest = 0  # To keep track of the longest sequence found
    counter = 1  # To count the current sequence length

    # Iterate through the sorted list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is exactly one more than the previous element
        if nums[i] - nums[i - 1] == 1:
            counter += 1  # Increment the counter for the current sequence
        # If the current element is the same as the previous element, do nothing
        elif nums[i] != nums[i - 1]:
            # Update the longest sequence length if the current sequence is longer
            longest = max(longest, counter)
            # Reset the counter for the new sequence
            counter = 1

    # After the loop, check the last sequence
    return max(longest, counter)



assert longestConsecutive(nums=[]) == 0
assert longestConsecutive(nums=[0,3,2,5,4,6,1,1]) == 7
assert longestConsecutive(nums = [2,20,4,10,3,4,5]) == 4