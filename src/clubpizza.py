n, c = (int(i) for i in input().split())
a = sorted(tuple(int(i) for i in input().split())[::-1] for _ in range(n))
res, vis = 0, set()
for p, t in a:
    if t in vis:
        continue
    if p > c:
        break
    res += 1
    c -= p
    vis.add(t)
print(res)
