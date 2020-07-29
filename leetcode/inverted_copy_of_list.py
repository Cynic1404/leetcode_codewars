# def revert(l):
#     res = []
#     for i in range(len(l)):
#         res.append(l[len(l)-1-i])
#     print(res)

def revert(l):
    res = [0]*len(l)
    for i in range(len(l)):
        res[i]=(l[len(l)-1-i])
    print(res)

revert(list('123456'))