h, w = (int(i) for i in input().split())
g = [list(input()) for _ in range(h)]
g[0][0] = 0
for r in range(h):
    for c in range(w):
        g[r][c] = int(g[r][c] == "I") + max(g[r - 1][c] if r else 0, g[r][c - 1] if c else 0)
res = g[-1][-1]
print(res)
