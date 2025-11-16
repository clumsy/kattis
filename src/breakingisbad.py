n = int(input())
res = 24 * 60
for _ in range(n):
    t = input().split()
    cur, e0 = 0, 24 * 60
    for c in t:
        s, e = c.split("-")
        h, m = (int(p.lstrip("0") or "0") for p in s.split(":"))
        s = 60 * h + m
        cur += max(0, s - e0)
        h, m = (int(p.lstrip("0") or "0") for p in e.split(":"))
        e0 = 60 * h + m
    res = min(res, cur)
print(res)
