from bisect import bisect_left


n, h = (int(input()) for _ in range(2))
p = sorted(tuple(int(i) for i in input().split()) for _ in range(n))
s = bisect_left(p, 0, key=lambda t: t[0])
res = 0
x0 = None
for i in range(s, n):
    x, y = p[i]
    if x0 is None or (y - h) * x0 > (y0 - h) * x:
        res += 1
        x0, y0 = x, y
x0 = None
while s:
    s -= 1
    x, y = p[s]
    if x0 is None or (y - h) * (-x0) > (y0 - h) * (-x):
        res += 1
        x0, y0 = x, y
print(res)
