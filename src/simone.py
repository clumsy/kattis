from collections import Counter


n, k = (int(i) for i in input().split())
cs = (int(i) for i in input().split())
cnt = Counter(cs)
for i in range(1, k + 1):
    if i not in cnt:
        cnt[i] = 0
res, mi = [], n
for k, v in cnt.items():
    if v < mi:
        res, mi = [], v
    if mi == v:
        res.append(k)
res.sort()
print(len(res))
print(*res)
