from collections import Counter


s = input()
cnt = Counter()
for v in "TCG":
    cnt[v] = 0
cnt.update(s)
res = sum(v ** 2 for v in cnt.values()) + 7 * min(cnt.values())
print(res)
