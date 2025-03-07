s, t, n = (int(i) for i in input().split())
d = (int(i) for i in input().split())
b = (int(i) for i in input().split())
c = (int(i) for i in input().split())
for _ in range(n):
    s += next(d)
    ci = next(c)
    s += ci - (s % ci) if s % ci else 0
    s += next(b)
s += next(d)
res = "yes" if s <= t else "no"
print(res)
