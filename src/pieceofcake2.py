n, h, v = (int(i) for i in input().split())
res = 4 * max(h * v, (n - h) * v, h * (n - v), (n - h) * (n - v))
print(res)
