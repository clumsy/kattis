xi, yi, xf, yf, xm1, ym1, xm2, ym2 = (int(i) for i in input().split())
rs, cs = xf - xi + 1, yf - yi + 1
dp = [[0] * cs for _ in range(rs)]
dp[0][0] = 1
mines = {(xm1, ym1), (xm2, ym2)}
for r in range(rs):
    for c in range(cs):
        if r == c == 0 or (xi + r, yi + c) in mines:
            continue
        dp[r][c] = (dp[r - 1][c] if r else 0) + (dp[r][c - 1] if c else 0)
res = dp[-1][-1]
print(res)
