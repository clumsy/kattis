n, q = (int(i) for i in input().split())
xs = {i + 1: int(e) for i, e in enumerate(input().split())}
for _ in range(q):
    t, c, x = (int(i) for i in input().split())
    if t == 1:
        xs[c] = x
    else:
        res = abs(xs[c] - xs[x])
        print(res)
