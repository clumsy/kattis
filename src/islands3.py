r, c = (int(i) for i in input().split())
g = [list(input()) for _ in range(r)]

def dfs(i, j):
    if g[i][j] == "W":
        return
    g[i][j] = "W"
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        i_, j_ = i + di, j + dj
        if 0 <= i_ < r and 0 <= j_ < c:
            dfs(i_, j_)

res = 0
for i in range(r):
    for j in range(c):
        if g[i][j] == "L":
            res += 1
            dfs(i, j)
print(res)
