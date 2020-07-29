def insert_sort(arr):
    n = len(arr)
    for top in range(1,n):
        k = top
        while k>0 and arr[k-1] > arr[k]:
            arr[k], arr[k-1] =  arr[k-1], arr[k]
            k -= 1
            print(arr)

insert_sort([13, 550, 543, 21, 2, 2331, 434, 12, 453, 1, 3, 432423, 54, 223])