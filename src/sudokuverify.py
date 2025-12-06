g = [input().replace(" ", "") for _ in range(9)]
res = "VALID"
for r in range(9):
    if len(set(g[r])) < 9:
        res = "INVALID!"
        break
for c in range(9):
    if len(set(g[r][c] for r in range(9))) < 9:
        res = "INVALID!"
        break
for b in range(9):
    r_, c_ = b // 3, 3 * (b % 3)
    s = g[3 * r_][c_ : c_ + 3] + g[3 * r_ + 1][c_ : c_ + 3] + g[3 * r_ + 2][c_ : c_ + 3]
    if len(set(s)) < 9:
        res = "INVALID!"
        break
print(res)
