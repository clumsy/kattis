t = int(input())
for _ in range(t):
    k = int(input())
    res, p = 0, 1
    while k:
        res += p
        p *= 2
        k -= 1
    print(res)
