rs, cs = (int(i) for i in input().split())
g = [input() for _ in range(rs)]
res = cnt = 0
for r in range(1, rs - 1):
    for c in range(1, cs - 1):
        if g[r][c] == "0" and g[r - 1][c - 1] == g[r - 1][c] == g[r - 1][c + 1] == g[r][c - 1] == g[r][c + 1] == g[r + 1][c - 1] == g[r + 1][c] == g[r + 1][c + 1] == "O":
            res = f"{r + 1} {c + 1}"
            cnt += 1
res = res if cnt == 1 else f"Oh no! {cnt} locations" if cnt > 0 else "Oh no!"
print(res)
