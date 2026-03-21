l, h, k = (int(i) for i in input().split())
g = [["_"] * l for _ in range(h)]
for i in range(k):
    ll, hh, x, y = (int(i) for i in input().split())
    s = chr(ord("a") + i)
    for r in range(hh):
        for c in range(ll):
            if y + r < h and x + c < l:
                g[y + r][x + c] = s
res = ["".join(r) for r in g]
print(*res, sep="\n")
