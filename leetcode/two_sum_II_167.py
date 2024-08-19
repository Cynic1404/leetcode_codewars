def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]