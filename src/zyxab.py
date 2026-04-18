n = int(input())
ss = (input() for _ in range(n))
res = None
for s in ss:
    if len(s) >= 5 and len(s) == len(set(s)):
        res = s if not res or len(s) < len(res) else max(res, s) if len(s) == len(res) else res
res = res or "Neibb"
print(res)
