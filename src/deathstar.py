n = int(input())
g = ((int(i) for i in input().split()) for _ in range(n))
res = [0] * n
for r, gr in enumerate(g):
    for c, e in enumerate(gr):
        if c >= r:
            res[r] |= e
            res[c] |= e
print(*res)
