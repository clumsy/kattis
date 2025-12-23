n, m = (int(i) for i in input().split())
res = [-i for i in range(1, n + 1)]
for _ in range(m):
    a, b = (int(i) - 1 for i in input().split())
    res[a] += 1
    res[b] += 1
print(*res)
