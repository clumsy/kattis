n = int(input())
s = [int(input()) for i in range(n)]
sm = []
for i, e in enumerate(s):
    sm.append((sm[-1] if sm else 0) + e * ((4 / 5) ** i) / 5)
res = []
for i, e in enumerate(s):
    res.append((sm[i - 1] if i else 0) + (sm[-1] - sm[i]) * (5 / 4))
res = sm[-1], sum(res) / n
print(*res, sep="\n")
