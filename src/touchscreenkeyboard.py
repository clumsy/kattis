d = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]
ds = {}
for r in range(3):
    for c in range(len(d[r])):
        k = d[r][c]
        ds[k] = (r, c)


def dst(s, t):
    res = 0
    for x, y in zip(s, t):
        res += abs(ds[x][0] - ds[y][0]) + abs(ds[x][1] - ds[y][1])
    return res


t = int(input())
for _ in range(t):
    s, l = input().split()
    res = []
    for _ in range(int(l)):
        t = input()
        res.append((dst(s, t), t))
    res = (f"{v} {r}" for r, v in sorted(res))
    print(*res, sep="\n")
