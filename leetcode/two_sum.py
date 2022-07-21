def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for b in range(i+1, len(nums)):
            if nums[i]+nums[b] == target:
                return [i, b]


def two_sum_fast(nums, target):
    new_dict = {}
    for _ in range(len(nums)):
        if target-nums[_] not in new_dict:
            new_dict[nums[_]] = _
        else:
            return [new_dict[target-nums[_]], _]



print(two_sum_bruteforce([3,3], 6))
print(two_sum_fast([3,3], 6))
print(two_sum_bruteforce([2,11,7,15], 9))
print(two_sum_fast([2,11,15,7], 9))