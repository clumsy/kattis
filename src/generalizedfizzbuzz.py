from math import lcm


n, a, b = (int(i) for i in input().split())
c = n // lcm(a, b)
res = n // a - c, n // b - c, c
print(*res)
