g = [input() for _ in range(3)]
res = "N"
if g[0][0] == g[1][1] == g[2][2] != "E" or g[2][0] == g[1][1] == g[0][2] != "E":
    res = g[1][1]
for i in range(3):
    if res != "N":
        break
    if g[i][0] == g[i][1] == g[i][2] != "E":
        res = g[i][0]
    elif g[0][i] == g[1][i] == g[2][i] != "E":
        res = g[0][i]
print(res)
