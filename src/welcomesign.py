r, c = (int(i) for i in input().split())
res, k = [], 0
for _ in range(r):
    s = input()
    d = c - len(s)
    h = d // 2
    if d & 1 == 0:
        s = "." * h + s + "." * h
    else:
        k += 1
        s = "." * (h + 1 - (k & 1)) + s + "." * (h + (k & 1))
    res.append(s)
print(*res, sep="\n")
