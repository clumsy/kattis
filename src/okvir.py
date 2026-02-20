m, n = (int(i) for i in input().split())
u, l, r, d = (int(i) for i in input().split())
s = [input() for _ in range(m)]
rs, cs = m + u + d, n + l + r
g = [[None] * cs for _ in range(rs)]
for r in range(rs):
    for c in range(cs):
        g[r][c] = "#" if (r + c) & 1 == 0 else "."
for r in range(u, u + m):
    for c in range(l, l + n):
        g[r][c] = s[r - u][c - l]
for r in g:
    res = "".join(r)
    print(res)
