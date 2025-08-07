from math import sqrt


xb, yb = (int(i) for i in input().split())
n = int(input())
res = "YES"
for _ in range(n):
    x, y = (int(i) for i in input().split())
    d = sqrt((x - xb) ** 2 + (y - yb) ** 2)
    res = "NO" if d <= 8 else res
print(res)
