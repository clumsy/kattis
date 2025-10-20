n, p = (int(i) for i in input().split())
bs = (int(i) for i in input().split())
res = cur = 0
for i in bs:
    cur = max(0, cur + i - p)
    res = max(res, cur)
print(res)
