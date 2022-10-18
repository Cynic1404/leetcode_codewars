def maxSubsequence(nums, k):
    sorted_by_max_value = sorted([[nums[i], i] for i in range(len(nums))], key=opa, reverse=True)[:k]
    sorted_by_index = sorted([[i[0], i[1]] for i in sorted_by_max_value], key=opa2)
    final = [i[0] for i in sorted_by_index]
    return final


def opa(element):
    return element[0]

def opa2(element):
    return element[1]

print(maxSubsequence([-1,-2,3,4], 3))
print(maxSubsequence([50, -75], 2))

