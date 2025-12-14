n = int(input())
res, vis = [], set()
for _ in range(n):
    s = input()
    if s not in vis:
        vis.add(s)
        res.append(s)
print(*res, sep="\n")
