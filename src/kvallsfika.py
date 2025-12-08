n, p, k = (int(input()) for _ in range(3))
c = (int(i) for i in input().split())
t = (int(i) for i in input().split())
ts, res = {}, 0
for ci, ti in sorted((ci, ti) for ci, ti in zip(c, t)):
    if ts.get(ti, 0) < k:
        if p < ci:
            break
        p -= ci
        ts[ti] = ts.get(ti, 0) + 1
        res += 1
print(res)
