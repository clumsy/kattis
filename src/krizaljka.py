a, b = input().split()
n = len(a)
ra, cb = next((b.find(a[c]), c) for c in range(n) if a[c] in b)
res = []
for r in range(len(b)):
    if r == ra:
        res.append(a)
    else:
        res.append("." * cb + b[r] + "." * (n - cb - 1))
print(*res, sep="\n")
