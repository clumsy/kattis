from math import inf


n, m = (int(i) for i in input().split())
g = [[int(i) for i in input().split()] for _ in range(n)]
res = "Neibb"
for r in range(1, n - 1):
    for c in range(1, m - 1):
        if g[r][c] < min(g[r - 1][c] if r else inf, g[r][c - 1] if c else inf,
                         g[r][c + 1] if c < m - 1 else inf, g[r + 1][c] if r < n - 1 else inf):
            res = "Jebb"
            break
print(res)
