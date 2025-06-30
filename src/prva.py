r, c = (int(i) for i in input().split())
ws = [*(input() + "#" for _ in range(r)), "#" * (c + 1)]
res = chr(ord("z") + 1) * max(r, c)
for c in range(len(ws[0])):
    w = []
    for r in range(len(ws)):
        if ws[r][c] == "#":
            if len(w) > 1:
                res = min(res, "".join(w))
            w = []
        else:
            w.append(ws[r][c])
for r in range(len(ws)):
    w = []
    for c in range(len(ws[0])):
        if ws[r][c] == "#":
            if len(w) > 1:
                res = min(res, "".join(w))
            w = []
        else:
            w.append(ws[r][c])
print(res)
