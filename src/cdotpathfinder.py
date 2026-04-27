n = int(input())
res = []
for _ in range(n):
    k = int(input())
    vs = [int(i) for i in input().split()]
    t = float("inf")
    for i in range(k):
        v, d = vs[2 * i], vs[2 * i + 1]
        if d / v < t:
            t, r = d / v, i + 1
    res.append(r)
print(*res, sep="\n")
