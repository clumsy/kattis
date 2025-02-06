n, p, s = (int(i) for i in input().split())
for _ in range(s):
    res = "REMOVE"
    m = (int(i) for i in input().split())
    for i, c in enumerate(m):
        if i > 0 and c == p:
            res = "KEEP"
    print(res)
