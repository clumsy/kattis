t = int(input())
for _ in range(t):
    a = (int(i) for i in input().split())
    res, p = 0, 1
    for i in a:
        res += max(0, i - 2 * p)
        p = i
    print(res)
