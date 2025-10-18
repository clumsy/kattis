from math import inf, gcd


n = int(input())
res = inf
for _ in range(n):
    y, c1, c2 = (int(i) for i in input().split())
    cur = y + c1 * (c2 // gcd(c1, c2))
    res = min(res, cur)
print(res)
