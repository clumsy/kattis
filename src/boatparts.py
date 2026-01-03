p, n = (int(i) for i in input().split())
res, has = None, set()
for i in range(n):
    s = input()
    has.add(s)
    if res is None and len(has) == p:
        res = i + 1
res = res or "paradox avoided"
print(res)
