from collections import Counter


h = input().split()
res = max(Counter(s[0] for s in h).values())
print(res)
