n, k = (int(input()) for _ in range(2))
res = []
if n < 2 or k == n:
    res.append("impossible")
else:
    for i in range(k):
        res.append(f"open {i + 1} using {i + 2}")
print(*res, sep="\n")
