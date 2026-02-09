n, m = (int(i) for i in input().split())
g = [input() for _ in range(n)]
res = 1
for c in range(m):
    res += all(g[r][c] == "_" for r in range(n))
print(res)
