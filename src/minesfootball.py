m = int(input())
ms = [[int(i) for i in input().split()] for _ in range(m)]
ml = mh = 0
li = hi = 1
lt, ht = float("inf"), 0
for i in range(m):
    ct = 0
    for j, e in enumerate(ms[i]):
        if j == 0:
            continue
        ct += e
        if e < ms[ml][li]:
            ml, li = i, j
        if e > ms[mh][hi]:
            mh, hi = i, j
    lt = min(lt, ct)
    ht = max(ht, ct)
res = ms[mh][hi], ms[ml][li], ht, lt
print(*res, sep="\n")
