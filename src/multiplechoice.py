n = int(input())
k = "".join(input() for _ in range(n))
m = int(input())
res = {}
for _ in range(m):
    id = int(input())
    res[id] = sum(i == j for i, j in zip(k, "".join(input() for _ in range(n))))
o = input()
rev = o.endswith("DESC")
grd = o.startswith("GRADE")


def key(t):
    if grd:
        return t[1] * (-1 if rev else 1), t[0]
    return t[0] * (-1 if rev else 1)


res = (f"{k} {v}" for k, v in sorted(res.items(), key=key))
print(*res, sep="\n")
