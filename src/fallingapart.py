n, a = int(input()), (int(i) for i in input().split())
res = [0, 0]
for i, e in enumerate(sorted(a, reverse=True)):
    res[i & 1] += e
print(*res)
