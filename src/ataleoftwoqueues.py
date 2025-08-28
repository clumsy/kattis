n, m = (int(i) for i in input().split())
ns = (int(i) for i in input().split())
ms = (int(i) for i in input().split())
d = sum(ns) - sum(ms)
res = "left" if d < 0 else "right" if d > 0 else "either"
print(res)
