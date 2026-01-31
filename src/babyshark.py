s = input().split()
prv = cur = 0
res = p = None
for w in s:
    if w != p:
        cur = 0
    cur += 1
    p = w
    if cur > prv:
        res, prv = w, cur
print(res)
