r, c = (int(i) for i in input().split())
g = [input() for _ in range(r)]
res = [0] * 5
for r_ in range(r - 1):
    for c_ in range(c - 1):
        if g[r_][c_] != "#" and g[r_][c_ + 1] != "#" and g[r_ + 1][c_] != "#" and g[r_ + 1][c_ + 1] != "#":
            cnt = (g[r_][c_] == "X") + (g[r_][c_ + 1] == "X") + (g[r_ + 1][c_] == "X") + (g[r_ + 1][c_ + 1] == "X")
            if cnt < 5:
                res[cnt] += 1
print(*res, sep="\n")
