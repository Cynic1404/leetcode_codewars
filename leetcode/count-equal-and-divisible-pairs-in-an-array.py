
def countPairs(nums,k):
    count = 0
    enum = sorted(enumerate(nums),key=lambda x:x[1])
    for i in range(1, max(nums)+1):
        res = list(filter(lambda x:x[1] == i, enum))
        for i in range(len(res)):
            for m in range(i+1, len(res)):
                if (res[i][0]*res[m][0])%k==0:
                    count+=1
    return count

print(countPairs(nums = [3,1,2,2,2,1,3], k = 2))



