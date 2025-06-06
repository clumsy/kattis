n = int(input())
res = None
for _ in range(n):
    t, o = (int(i) for i in input().split())
    if o == 0:
        res = min(res, (o, t)) if res else (o, t)
res = res[1] if res else -1
print(res)
