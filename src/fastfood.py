t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    ps = []
    for _ in range(n):
        k, *ts, p = (int(i) for i in input().split())
        ps.append((ts, p))
    cnt = {i + 1: int(e) for i, e in enumerate(input().split())}
    res = 0
    for ts, p in ps:
        if ts:
            d = float("inf")
            for t in ts:
                d = min(d, cnt.get(t, 0))
            res += d * p
    print(res)
