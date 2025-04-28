def count(x, s):
    lx, ls = len(x), len(s)
    res = sum(i == j for i, j in zip(x * ((ls + lx - 1) // lx), s))
    return res

n, s = int(input()), input()
res, ma = {}, 0
for i, v in (
    ("Adrian", count("ABC", s)),
    ("Bruno", count("BABC", s)),
    ("Goran", count("CCAABB", s)),
):
    res[v] = res.get(v, [])
    res[v].append(i)
    ma = max(ma, v)
res = sorted(res[ma])
print(ma)
print(*res, sep="\n")
