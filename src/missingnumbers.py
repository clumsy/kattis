n = int(input())
a = (int(input()) for _ in range(n))
res, p, i = [], next(a), 0
while p:
    i += 1
    if p == i:
        p = next(a, None)
    else:
        res.append(i)
res = res or ["good job"]
print(*res, sep="\n")
