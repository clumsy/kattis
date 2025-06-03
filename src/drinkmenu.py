n, m = (int(i) for i in input().split())
dks = {i: input() for i in range(n)}
cnt = {}
res = []
for _ in range(m):
    c = input()
    cnt[c] = cnt.get(c, 0) + 1
    res.append(dks[cnt[c] - 1])
print(*res, sep="\n")
