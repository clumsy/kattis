from bisect import insort


jx, jy = (int(i) for i in input().split())
ds = [[], []]
for i in range(2):
    for _ in range(6):
        x, y = (int(i) for i in input().split())
        insort(ds[i], (jx - x) ** 2 + (jy - y) ** 2)
ds = [ds[0][::-1], ds[1][::-1]]
res = k = 0
while ds[0] and ds[1]:
    d = ds[0][-1] - ds[1][-1]
    if d <= 0:
        ds[0].pop()
    if d >= 0:
        ds[1].pop()
    res = res or d
    if res * d > 0:
        k += 1
    elif res * d <= 0:
        break
res = ("JONNA", k) if res < 0 else ("OPPONENTS", k) if res > 0 else ("TIE",)
print(*res, sep="\n")
