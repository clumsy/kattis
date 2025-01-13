from collections import Counter


n, m = (int(i) for i in input().split())
cnt = Counter()
for i in range(n):
    for j in range(m):
        cnt[i + 1 + j + 1] += 1
ma = max(cnt.values())
res = sorted([k for k, v in cnt.items() if v == ma])
print(*res, sep="\n")
