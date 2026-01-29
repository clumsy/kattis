n, p = int(input()), (int(i) for i in input().split())
p = sorted(p, reverse=True)
res = 0
for i in range(2, n, 3):
    res += p[i]
print(res)
