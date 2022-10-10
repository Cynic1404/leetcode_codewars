def reverse_list(num):
    start_index = 0
    end_index = -1
    for i in range(len(num)//2):
        # num[start_index], num[end_index] = num[end_index], num[start_index]
        # start_index+=1
        # end_index-=1
        num[i], num[len(num)-1-i] = num[len(num)-1-i], num[i]

    print(num)


reverse_list([1,2,3,4,5,6,7,8])