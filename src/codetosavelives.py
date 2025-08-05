t = int(input())
for _ in range(t):
    f, s = (input().split() for _ in range(2))
    res, c = [], 0
    while f or s or c:
        n = (int(f.pop()) if f else 0) + (int(s.pop()) if s else 0) + c
        c, n = divmod(n, 10)
        res.append(str(n))
    res = " ".join(res[::-1])
    print(res)
