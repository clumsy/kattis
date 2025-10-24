n, lph = (int(i) for i in input().split())
ls = (int(input()) for _ in range(n))
res, locs = 0, lph * 5
for l in sorted(ls):
    if l > locs:
        break
    res += 1
    locs -= l
print(res)
