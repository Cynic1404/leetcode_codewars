#brute force
# def maxArea(height):
#     max_area = 0
#     for left in range(len(height)):
#         for right in range(left + 1, len(height)):
#             area = min(height[right], height[left]) * (right - left)
#             max_area = max(area, max_area)
#     return max_area

def maxArea(height):
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        min_height = min(height[left], height[right])
        area = min_height * (right - left)
        max_area = max(max_area, area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area

assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([1,1]) == 1