t, n = (int(i) for i in input().split())
s = sorted(int(i) for i in input().split())
t *= 60
res = 0
for c in s:
    t -= c
    if t < 0:
        break
    res += c
print(res)
