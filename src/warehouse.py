t = int(input())
for _ in range(t):
    n = int(input())
    res = {}
    for _ in range(n):
        k, v = input().split()
        res[k] = res.get(k, 0) + int(v)
    print(len(res))
    res = (f"{k} {v}" for k, v in sorted(res.items(), key=lambda t: (-t[1], t[0])))
    print(*res, sep="\n")
