n, a = int(input()), (int(i) for i in input().split())
res = []
for i in a:
    if not res or i > res[-1]:
        res.append(i)
print(len(res))
print(*res)
