ps = [True] * 101
ps[0] = ps[1] = False
for i in range(len(ps)):
    if ps[i]:
        for j in range(2 * i, len(ps), i):
            ps[j] = False
res = [i for i, v in enumerate(ps) if v]
print(*res, sep="\n")
