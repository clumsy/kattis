a, b = (int(i) for i in input().split())
ab = min(a, b)
a -= ab
a3 = a // 3
a -= a3 * 3
a2 = a // 2
a -= a2 * 2
res = ab * 10 + a3 * 10 + a2 * 3 + a
print(res)
