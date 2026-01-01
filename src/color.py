s, c, k = (int(i) for i in input().split())
d = (int(i) for i in input().split())
prv = cnt = float("inf")
res = 0
for i in sorted(d):
    cnt += 1
    if cnt > c or i - prv > k:
        res += 1
        cnt = 0
        prv = i
print(res)
