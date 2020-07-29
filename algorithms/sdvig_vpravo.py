def sdvig_vlevo(arr):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=tmp
    print(arr)

# sdvig_vlevo([1,2,3,4,5,6,7,8,9,10])

def sdvig_vpravo(arr):
    tmp = arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0] = tmp
    print(arr)

sdvig_vpravo([1,2,3,4,5,6,7,8,9,10])