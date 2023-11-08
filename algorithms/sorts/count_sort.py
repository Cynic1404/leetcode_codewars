def count_sort(arr):
    d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in arr:
        d[i]=d[i]+1

    res=[]
    for i in d:

        res+=[i]*d[i]
    print(res)


count_sort([1,2,3,4,5,3,4,7,9,7,4,5,6,8])