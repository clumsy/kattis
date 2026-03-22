n = int(input())
res = m = 2
while True:
    res, i = m, 2
    while i * i <= m * n:
        if divmod(m * n, i * i)[1] == 0:
            res = -1
            break
        i += 1
    if res > 0:
        break
    m += 1
print(res)
