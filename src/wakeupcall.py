n, m = (int(i) for i in input().split())
ns = (int(i) for i in input().split())
ms = (int(i) for i in input().split())
d = sum(ns) - sum(ms)
res = "Button 1" if d > 0 else "Button 2" if d < 0 else "Oh no"
print(res)
