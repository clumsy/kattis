n = int(input())
while True:
    n += 1
    s, r = n * n, 0
    while s and r != 6:
        s, r = divmod(s, 10)
    if r != 6:
        res = n
        break
print(res)
