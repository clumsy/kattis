n, m = (int(i) for i in input().split())
o, ms, res = 0, {}, ["stolen!"] * n
for _ in range(n + m):
    s = input()
    if s in ms:
        o += 1
        res[ms[s]] = o
    else:
        ms[s] = len(ms)
print(*res, sep="\n")
