from collections import Counter


s, n = input(), int(input())
ws = (input() for _ in range(n))
cnt = Counter(s)
res = []
for w in ws:
    if len(w) < 4 or s[0] not in w:
        continue
    cnt_ = Counter(w)
    if all(c in cnt for c in cnt_):
        res.append(w)
print(*res, sep="\n")
