from collections import Counter


s = input()
cnt = Counter(s)
res = max(0, sum(i & 1 for i in cnt.values()) - 1)
print(res)
