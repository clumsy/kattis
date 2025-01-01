n = int(input())
p = (int(input()) for _ in range(n))
mi = ma = next(p)
for i in p:
    mi = min(mi, i)
    ma = max(ma, i)
res = mi - min(ma // 2, mi)
print(res)
