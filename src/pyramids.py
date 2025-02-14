n = int(input())
res, i = 0, 1
while n >= i ** 2:
    res += 1
    n -= i ** 2
    i += 2
print(res)
