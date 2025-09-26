c, k = (int(i) for i in input().split())
k = 10 ** k
d, r = divmod(c, k)
res = d * k + k * ((r + k // 2) // k)
print(res)
