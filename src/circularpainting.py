from math import pi


n = int(input())
res = 0
for _ in range(n):
    d, r1, r2 = (int(i) for i in input().split())
    res += pi * (r2**2 - r1**2) * d / 360
print(res)
