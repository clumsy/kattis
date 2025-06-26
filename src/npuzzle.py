pos = {chr(ord("A") + i): (i // 4, i % 4) for i in range(26)}
res = 0
for r in range(4):
    s = input()
    for c, v in enumerate(s):
        if v != ".":
            x, y = pos[v]
            res += abs(x - r) + abs(y - c)
print(res)
