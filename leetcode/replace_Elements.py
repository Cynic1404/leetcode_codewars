def replaceElements(arr):
    max_number = 0
    min_index = 0
    max_index = 0
    while max_index < len(arr) - 1:
        for i in range(max_index + 1, len(arr)):
            if arr[i] > max_number:
                max_number = arr[i]
                max_index = i
        for m in range(min_index, max_index):
            arr[m] = max_number
        max_number = 0
        min_index = max_index
    arr[-1] = -1
    return arr


assert replaceElements([17,18,5,4,6,1]) == [18,6,6,6,1,-1]
