n = int(input())
res = []
for i in range(n):
    vs = (int(i) for i in input().split())
    for j, v in enumerate(vs):
        if v >= 0:
            res.append((i + 1, j + 1, v))
print(len(res))
for r in res:
    print(*r)
