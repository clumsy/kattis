from math import sqrt


# 2h + a = x
# 2h + b = y
# a * b * h = (x - 2h)(y - 2h)*h -> max
# (xy - 2hx - 2hy + 4h^2)h -> max
# 4h^3 - 2h^2(x + y) + hxy -> max
# 12h^2 - 4h(x + y) + xy = 0
# D = 4(x + y) ^ 2 - xy
# h1,h2 = (2 * (x + y) +/- D)/12
t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    d = sqrt(4 * ((x + y) ** 2) - 12 * x * y)
    h1 = (2 * (x + y) - d) / 12
    h2 = (2 * (x + y) + d) / 12
    res = 0.
    for h in (h1, h2):
        if h > 0:
            res = max(res, (x - 2 * h) * (y - 2 * h) * h)
    print(res)
