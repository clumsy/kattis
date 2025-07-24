from collections import defaultdict


n = int(input())
cnt = defaultdict(set)
for _ in range(n):
    s = input().split()
    cnt[s[-1]].add("".join(s[:-1]))
res = (f"{k} {len(cnt[k])}" for k in sorted(cnt.keys()))
print(*res, sep="\n")
