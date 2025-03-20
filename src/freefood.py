n = int(input())
ds = [0] * 366
for _ in range(n):
    s, t = (int(i) for i in input().split())
    ds[s - 1] += 1
    ds[t] -= 1
res = cur = 0
for i, d in enumerate(ds):
    cur += d
    res += cur > 0
print(res)
