pa, ka, pb, kb, n = (int(i) for i in input().split())
res = float("inf")
for i in range((n + ka - 1) // ka + 1):
    j = (n - ka * i + kb - 1) // kb
    cur = i * pa + j * pb
    if cur < res:
        res, a, b = cur, i, j
res = a, b, res
print(*res)
