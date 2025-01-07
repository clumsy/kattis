m = (sum(int(i) for i in input().split()) for _ in range(5))
res = 0, 0
for r, v in enumerate(m):
    if v > res[1]:
        res = r + 1, v
print(*res)
