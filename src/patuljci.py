ds = [int(input()) for _ in range(9)]
res, s = None, sum(ds)
for i in range(8):
    if res:
        break
    for j in range(i + 1, 9):
        if s - (ds[i] + ds[j]) == 100:
            res = [ds[k] for k in range(9) if k != i and k != j]
            break
print(*res, sep="\n")
