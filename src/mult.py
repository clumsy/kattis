from math import gcd

n = int(input())
f = None
for _ in range(n):
    res = int(input())
    if f is None:
        f = res
    elif gcd(f, res) == f:
        print(res)
        f = None
