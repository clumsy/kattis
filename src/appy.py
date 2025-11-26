n = int(input())
res, usd = [], set()
for _ in range(n):
    m, *s = input().split()
    for a in s:
        if a not in usd:
            res.append(a)
            usd.add(a)
            break
res = " ".join(res)
print(res)
