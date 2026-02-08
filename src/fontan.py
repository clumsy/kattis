n, m = (int(i) for i in input().split())
g = []


def dfs(c, r):
    if not (0 <= r < n) or not (0 <= c < m):
        return
    g[r][c] = "V"
    if r + 1 < n and g[r + 1][c] == ".":
        dfs(c, r + 1)
    elif r + 1 < n and g[r + 1][c] == "#":
        if c - 1 >= 0 and g[r][c - 1] == ".":
            dfs(c - 1, r)
        if c + 1 < m and g[r][c + 1] == ".":
            dfs(c + 1, r)


for _ in range(n):
    g.append(list(input()))
for r in range(n):
    for c in range(m):
        if g[r][c] == "V":
            dfs(c, r)
for r in g:
    res = "".join(r)
    print(res)
