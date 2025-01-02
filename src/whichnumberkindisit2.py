from math import isqrt


t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    if n & 1 == 1:
        res.append("O")
    if isqrt(n) ** 2 == n:
        res.append("S")
    if not res:
        res.append("EMPTY")
    res = "".join(res)
    print(res)
