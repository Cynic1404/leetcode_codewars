def maxSubsequence(nums, k):
    sorted_by_max_value = sorted([[nums[i], i] for i in range(len(nums))], reverse=True)[:k]
    sorted_by_index = sorted([[i[1], i[0]] for i in sorted_by_max_value])
    final = [i[1] for i in sorted_by_index]
    return final


assert maxSubsequence([-1,-2,3,4], 3) == [-1,3,4]
assert maxSubsequence([50, -75], 2) == [50, -75]

