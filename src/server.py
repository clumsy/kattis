n, t = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = 0
for i in a:
    t -= i
    if t < 0:
        break
    res += 1
print(res)
