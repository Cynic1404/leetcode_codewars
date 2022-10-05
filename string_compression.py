def compress(s):
    st = ''
    checker = {}
    for i in s:
        if i in checker:
            checker[i]=checker[i]+1
        else:
            checker[i]=1
    for l, m in checker.items():
        st+=l+str(m)
    return(st)

# def compress(s):
#     if not len(s):
#         return ""
#     new_st=''
#     counter=0
#     new_letter=None
#     for i in s:
#         if not new_letter:
#             new_letter=i
#             counter=1
#         else:
#             if new_letter == i:
#                 counter+=1
#             else:
#                 new_st+=new_letter+str(counter)
#                 new_letter = i
#                 counter = 1
#     new_st+=new_letter+str(counter)
#     return(new_st)