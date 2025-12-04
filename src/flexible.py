w, p = (int(i) for i in input().split())
ps = [0] + [int(i) for i in input().split()] + [w]
p = len(ps)
res = set()
for i in range(p - 1):
    for j in range(i + 1, p):
        res.add(ps[j] - ps[i])
res = sorted(res)
print(*res)
