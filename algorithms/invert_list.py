

def revert(l):
    for i in range(len(l)//2):
        l[i],l[-i-1]=l[-i-1],l[i]
    print(l)

def revert2(l):
    le = len(l)
    for i in range(le // 2):
        l[i], l[le - 1-i] = l[le-1-i], l[i]
    print(l)

# def revert(l):
#     res=[0]*len(l)
#     for i in range(len(l)//2):
#         res[i],l[len(l)-1-i]=l[len(l)-1-i],res[i]
#     print(res)
a = [1,2,3,4,5,6,7,8,9,10]
b = list(a)

revert(a)
revert2(b)