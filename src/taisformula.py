n = int(input())
t0 = v0 = res = 0
for _ in range(n):
    t, v = (float(f) for f in input().split())
    if t0 > 0:
        res += (v + v0) / 2 * (t - t0)
    t0, v0 = t, v
res /= 1000
print(res)
