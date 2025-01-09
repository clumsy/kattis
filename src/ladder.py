from math import sin, ceil, pi

h, v = (int(i) for i in input().split())
res = ceil(h / sin((v * pi) / 180))
print(res)
