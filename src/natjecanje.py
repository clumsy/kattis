n, s, r = (int(i) for i in input().split())
ss = (int(i) for i in input().split())
rs = (int(i) for i in input().split())
res = [True] * n
for i in ss:
    res[i - 1] = False
for i in rs:
    if not res[i - 1]:
        res[i - 1] = True
    elif i > 1 and not res[i - 2]:
        res[i - 2] = True
    elif i < n and not res[i]:
        res[i] = True
res = sum(not i for i in res)
print(res)
