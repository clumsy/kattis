from math import log, ceil


t = int(input())
for _ in range(t):
    p, r, f = (int(i) for i in input().split())
    # p * r ^ x = f => x = log r (f/p)
    res = 0 if r <= 1 or p > f else ceil(log((f + 1) / p, r))
    print(res)
