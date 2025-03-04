p = int(input())
for _ in range(p):
    k, b, n = (int(i) for i in input().split())
    res = 0
    while n:
        n, r = divmod(n, b)
        res += r ** 2
    res = k, res
    print(*res)
