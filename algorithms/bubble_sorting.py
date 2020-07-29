count=0

# def bubble_sorting(arr):
#     global count
#     for i in range(len(arr)-1):
#         for v in range(len(arr)-i-1):
#             print(v)
#             if arr[v]>arr[v+1]:
#                 arr[v], arr[v+1]=arr[v+1], arr[v]
#             count+=1
#         print(arr)
#     print(count)
#


#
#
#
#
#
#
# def bubble_sorting(arr):
#     global count
#     for i in range(1, len(arr)):
#         for v in range(len(arr)-i):
#             if arr[v]>arr[v+1]:
#                 arr[v], arr[v+1]=arr[v+1], arr[v]
#             count+=1
#
#     print(arr, count)
#
#




def bubble_sorting(arr):
    for i in range(1, len(arr)):
        for v in range(0, len(arr)-i):
            if arr[v]>arr[v+1]:
                arr[v], arr[v+1] = arr[v+1], arr[v]

    print(arr)





bubble_sorting([550,13,543,21, 1,7,2,4,19,78, 89,23456, 345])
# bubble([550,13,543,21, 1,7,2,4])
