r, c = (int(i) for i in input().split())
g = [input() for _ in range(r)]
res = 0
for i in range(r):
    for j in range(c):
        res += g[i][j] == "W" and (
            (i > 0 and g[i - 1][j] == "O")
            or (j > 0 and g[i][j - 1] == "O")
            or (i < r - 1 and g[i + 1][j] == "O")
            or (j < c - 1 and g[i][j + 1] == "O")
        )
print(res)
