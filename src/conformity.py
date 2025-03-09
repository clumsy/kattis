from collections import Counter


n = int(input())
unq, cnt, res = Counter(), Counter(), 0
for _ in range(n):
    s = "".join(sorted(input().split()))
    unq[s] += 1
    cnt[unq[s]] += 1
    res = max(res, cnt[unq[s]])
print(res)
