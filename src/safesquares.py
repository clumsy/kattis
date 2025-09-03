g = [input() for _ in range(8)]
rs1, rs2 = set(), set()
for r in range(8):
    for c in range(8):
        if g[r][c] == "R":
            rs1.add(c)
            rs2.add(r)
res = 0
for r in range(8):
    for c in range(8):
        res += (c not in rs1) and (r not in rs2)
print(res)
