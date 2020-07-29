def kWeakestRows(mat, k):
    res = {}
    na = []

    for i in range(len(mat)):
        s = sum(mat[i])
        if s not in res:
            res[s]=[i]
        else:
            res[s].append(i)
    for i in sorted(list(res)):
        na+=res[i]
        if len(na)>=k:
            return na[:k]


print(kWeakestRows(mat =
[[1,0],[1,0],[1,0],[1,1]],

k = 4))