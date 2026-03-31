from bisect import insort


n = int(input())
q = []
for _ in range(n):
    m, *lr = (int(i) for i in input().split())
    for i in range(m):
        l, r = lr[2 * i], lr[2 * i + 1]
        insort(q, (l, +1))
        insort(q, (r + 1, -1))
cur = ma = 0
res = {}
for t, d in q:
    cur += d
    if cur >= ma:
        ma, beg = cur, t
    if d < 0 and cur + 1 == ma:
        res[ma] = res.get(ma, 0) + (t - beg)
res = ma, res[ma]
print(*res, sep="\n")
