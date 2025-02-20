from math import sqrt


m = int(input())
rs, cs = [], []
for _ in range(m):
    t, *rst = input().split()
    (rs if t == "rectangle" else cs).append(tuple(int(i) for i in rst))
n = int(input())
for _ in range(n):
    x, y = (int(i) for i in input().split())
    res = 0
    for x1, y1, x2, y2 in rs:
        res += x1 <= x <= x2 and y1 <= y <= y2
    for x0, y0, r in cs:
        res += sqrt((x - x0) ** 2 + (y - y0) ** 2) <= r
    print(res)
