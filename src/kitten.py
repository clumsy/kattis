k = int(input())
m = {}
while True:
    a = [int(i) for i in input().split()]
    if a[0] == -1:
        break
    for i in a[1:]:
        m[i] = a[0]
res = []
while k in m:
    res.append(k)
    k = m[k]
res.append(k)
print(*res)
