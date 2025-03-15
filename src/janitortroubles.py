from math import sqrt


a, b, c, d = (int(i) for i in input().split())
p = (a + b + c + d) / 2
res = sqrt((p - a) * (p - b) * (p - c) * (p - d))
print(res)
