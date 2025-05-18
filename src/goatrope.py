from math import sqrt

x, y, x1, y1, x2, y2 = (int(i) for i in input().split())
if x1 <= x <= x2:
    res = min(abs(y - y1), abs(y - y2))
elif y1 <= y <= y2:
    res = min(abs(x - x1), abs(x - x2))
else:
    res = min(
        sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2),
        sqrt(abs(x - x2) ** 2 + abs(y - y2) ** 2),
        sqrt(abs(x - x1) ** 2 + abs(y - y2) ** 2),
        sqrt(abs(x - x2) ** 2 + abs(y - y1) ** 2),
    )
print(res)
