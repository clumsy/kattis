n = int(input())
res, i = 0, 1
while i ** 3 < n:
    res += i * (i + 1) * (i + 2) < n
    i += 1
print(res)
