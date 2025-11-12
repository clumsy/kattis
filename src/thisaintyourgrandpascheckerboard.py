n = int(input())
g = [input() for _ in range(n)]
res = 1
for r in range(n):
    b = w = 0
    for c in range(n):
        b += g[r][c] == "B"
        w += g[r][c] == "W"
        if c > 1 and g[r][c] == g[r][c - 1] == g[r][c - 2]:
            res = 0
            break
    if b != w:
        res = 0
    if res == 0:
        break
for c in range(n):
    b = w = 0
    for r in range(n):
        b += g[r][c] == "B"
        w += g[r][c] == "W"
        if r > 1 and g[r][c] == g[r - 1][c] == g[r - 2][c]:
            res = 0
            break
    if b != w:
        res = 0
    if res == 0:
        break
print(res)
