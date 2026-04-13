w, h = (int(i) for i in input().split())
g, nxt = [], []
for r in range(h):
    g.append(list(input()))
    for c in range(w):
        if g[r][c] == "*":
            nxt.append((r, c))
res, i = None, -1
while nxt:
    i += 1
    cur, nxt = nxt, []
    while cur:
        r, c = cur.pop()
        if g[r][c] == "E":
            res = i
            break
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            r_, c_ = r + dr, c + dc
            if 0 <= r_ < h and 0 <= c_ < w:
                if g[r_][c_] == "D":
                    nxt.append((r_, c_))
                elif g[r_][c_] in ".E":
                    cur.append((r_, c_))
                g[r_][c_] = "#" if g[r_][c_] != "E" else "E"
res = res if res is not None else "NOT POSSIBLE"
print(res)
