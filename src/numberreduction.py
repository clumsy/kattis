n = int(input())
res = 0
while n > 1:
    res += 1
    if n & 1 == 0:
        n >>= 1
    else:
        n += 2 * n + 1
print(res)
