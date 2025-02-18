def sd(i):
    res = 0
    while i:
        i, d = divmod(i, 10)
        res += d
    return res

while True:
    n = int(input())
    if n == 0:
        break
    res, t = 11, sd(n)
    while True:
        if t == sd(res * n):
            break
        res += 1
    print(res)
