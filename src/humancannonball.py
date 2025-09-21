from heapq import heappop, heappush
from math import sqrt, inf


x0, y0 = (float(i) for i in input().split())
xn, yn = (float(i) for i in input().split())
n = int(input())
xs = [tuple(float(i) for i in input().split()) for _ in range(n)]
xs.append((xn, yn))
dst = {}

def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

q = [(0, False, x0, y0)]
while q:
    t, c, x, y = heappop(q)
    if x == xn and y == yn:
        res = t
        break
    for i in range(n + 1):
        d = min(
            t + dist((x, y), xs[i]) / 5,
            t + 2 + abs(dist((x, y), xs[i]) - 50) / 5 if c else inf
        )
        if d < dst.get(i, inf):
            dst[i] = d
            heappush(q, (d, i < n, *xs[i]))
print(res)
