from math import gcd


n, d = (int(i) for i in input().split())
a = (int(i) for i in input().split())
g = gcd(n, d)
res = sum(v for i, v in enumerate(a) if i % g == 0)
print(res)
