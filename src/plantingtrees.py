n, a = int(input()), (int(i) for i in input().split())
res = 0
for i, e in enumerate(sorted(a, reverse=True)):
    res = max(res, e + i + 2)
print(res)
