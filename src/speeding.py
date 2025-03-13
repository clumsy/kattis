n = int(input())
res = 0
for _ in range(n):
    t, d = (int(i) for i in input().split())
    if t > 0:
        res = max(res, (d - d0) // (t - t0))
    t0, d0 = t, d
print(res)
