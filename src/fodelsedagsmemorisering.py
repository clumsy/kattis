t = int(input())
res = {}
for _ in range(t):
    s, c, b = input().split()
    c = int(c)
    res[b] = res[b] if b in res and res[b][1] > c else (s, c)
res = sorted(r[0] for r in res.values())
print(len(res))
print(*res, sep="\n")
