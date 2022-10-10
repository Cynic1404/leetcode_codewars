def reverse_list(num):
    start_index = 0
    end_index = -1
    for i in range(len(num)//2):
        num[start_index], num[end_index] = num[end_index], num[start_index]
        start_index+=1
        end_index-=1

    print(num)


reverse_list(["A", "b", "c", "d", "e", "f"])