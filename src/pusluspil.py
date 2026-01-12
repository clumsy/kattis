n, m = (int(i) for i in input().split())
res = set()
for _ in range(n):
    s = (int(i) for i in input().split())
    next(s)
    res |= set(s)
res = "Jebb" if len(res) == m else "Neibb"
print(res)
