from math import sqrt


n = int(input())
x, y = (int(i) for i in input().split())
r2 = sqrt(2)
for _ in range(n - 1):
    d, r = input().split()
    r = int(r)
    x = x + r if d == "E" else x - r if d == "W" else x
    x = x + r / r2 if d == "SE" or d == "NE" else x - r / r2 if d == "SW" or d == "NW" else x
    y = y + r if d == "N" else y - r if d == "S" else y
    y = y + r / r2 if d == "NE" or d == "NW" else y - r / r2 if d == "SW" or d == "SE" else y
res = x, y
print(*res)
