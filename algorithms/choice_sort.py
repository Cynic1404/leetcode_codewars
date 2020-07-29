def choice_sort(arr):
    for i in range(len(arr)-1):
        for v in range(i+1, len(arr)):
            if arr[i]>arr[v]:
                arr[i],arr[v]=arr[v],arr[i]

            print(arr)



choice_sort([550, 13, 543, 21, 2, 2331, 434, 12, 453, 3, 432423, 54, 223,1])