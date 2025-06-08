t = int(input())
for _ in range(t):
    n, x = int(input()), (int(i) for i in input().split())
    ma = mi = next(x)
    for i in x:
        mi, ma = min(mi, i), max(ma, i)
    res = 2 * (ma - mi)
    print(res)
