from collections import defaultdict


n, a = int(input()), [int(i) for i in input().split()]
cnt = defaultdict(int)
for e in a:
    cnt[e] = 1 if cnt[e] == 0 else -1
res = "none"
for i, e in enumerate(a):
    if cnt[e] == 1 and (res == "none" or e > a[res - 1]):
        res = i + 1
print(res)
