from math import floor


g, t, n = (int(i) for i in input().split())
w = (int(i) for i in input().split())
res = floor(0.9 * (g - t) - sum(w))
print(res)
