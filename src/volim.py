k, n = (int(input()) for _ in range(2))
ts = (input().split() for _ in range(n))
r = 3 * 60 + 30
res = k
for i in range(n):
    t, s = next(ts)
    r -= int(t)
    if r <= 0:
        continue
    if s == "T":
        res = res % 8 + 1
print(res)
