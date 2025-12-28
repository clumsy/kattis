g = [[None] * 8 for _ in range(8)]
w = (input() for _ in range(2))
for i, v in enumerate(w):
    for p in v.replace("White: ", "").replace("Black: ", "").split(","):
        if not p:
            continue
        p = p if len(p) == 3 else "P" + p
        c, r = ord(p[1]) - ord("a"), 8 - int(p[2])
        g[r][c] = p[0] if i == 0 else p[0].lower()
line = "---".join(["+"] * 9)
res = [line]
for r in range(8):
    row = []
    for c in range(8):
        clr = "." if (r + c) & 1 == 0 else ":"
        row.append(f"{clr}{g[r][c] or clr}{clr}")
    res.append("|" + "|".join(row) + "|")
    res.append(line)
print(*res, sep="\n")
