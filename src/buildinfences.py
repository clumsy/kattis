from math import inf


n = int(input())
xl = yl = inf
xr = yr = -inf
for _ in range(n):
    x, y = (int(i) for i in input().split())
    xl, xr = min(xl, x), max(xr, x)
    yl, yr = min(yl, y), max(yr, y)
res = 2 * (xr - xl + 2 + yr - yl + 2)
print(res)
