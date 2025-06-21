n, m, q = (int(i) for i in input().split())
res = [[i + 1, input()] for i in range(n)]
m = 0
for _ in range(q):
    i, a = input().split()
    for j, e in enumerate(res):
        if e[0] > 0 and e[1][int(i) - 1] != a:
            res[j][0] = 0
res = [i for i, e in res if i > 0]
res = ["unique", res.pop()] if len(res) == 1 else ["ambiguous", len(res)]
print(*res, sep="\n")
