from collections import Counter


n, m = (int(i) for i in input().split())
cnt, ma = Counter(), None
for _ in range(n):
    t = int(input())
    cnt[t] += 1
    if ma is None or cnt[t] > cnt[ma]:
        ma = t
res = "Ja" if m >= n - cnt[ma] else "Nej"
print(res)
