t = int(input())
for _ in range(t):
    n = int(input())
    res, trq = 0, -float("inf")
    for i in range(n):
        a, b, c = (int(i) for i in input().split())
        # -2ar + b = 0 => r = b / 2a
        r = b / (2 * a)
        cur = - a * (r ** 2) + b * r + c
        if cur > trq:
            res, trq = i + 1, cur
    print(res)
