n = int(input())
a = (int(i) for i in input().split())
mi = ma = next(a)
for t in a:
    mi = min(mi, t)
    ma = max(ma, t)
res = ma, mi
print(*res)
