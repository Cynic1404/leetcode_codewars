
def longestConsecutive(nums):
    # If the list is empty, return 0
    if not nums:
        return 0

    # Sort the list
    nums = sorted(nums)

    # Initialize the variables
    longest = 0  # To keep track of the longest sequence found
    counter = 1  # To count the current sequence length


    for i in range(1, len(nums)):    # Iterate through the sorted list starting from the second element
        if nums[i] - nums[i - 1] == 1: # If the current element is exactly one more than the previous element
            counter += 1  # Increment the counter for the current sequence
        elif nums[i] != nums[i - 1]: # If the current element is the same as the previous element, do nothing
            longest = max(longest, counter) # Update the longest sequence length if the current sequence is longer
            counter = 1 # Reset the counter for the new sequence
    return max(longest, counter)     # After the loop, check the last sequence


# fastest
def longestConsecutive(nums):
    if not nums:  # Check if the list is empty
        return 0  # Return 0 if the list is empty

    longest = 0  # Initialize the longest sequence length
    nums = set(nums)  # Convert the list to a set for O(1) average-time complexity checks

    for num in nums:  # Iterate through each number in the set
        if num - 1 not in nums:  # Check if the current number is the start of a sequence
            streak = 1  # Initialize the current sequence length
            current_num = num  # Initialize the current number in the sequence

            while current_num + 1 in nums:  # Continue the sequence as long as the next number is in the set
                current_num += 1  # Move to the next number
                streak += 1  # Increment the sequence length

            longest = max(longest, streak)  # Update the longest sequence length if the current sequence is longer

    return longest  # Return the length of the longest consecutive sequence



assert longestConsecutive(nums=[]) == 0
assert longestConsecutive(nums=[0,3,2,5,4,6,1,1]) == 7
assert longestConsecutive(nums = [2,20,4,10,3,4,5]) == 4