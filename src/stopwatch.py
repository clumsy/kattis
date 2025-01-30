n = int(input())
res, s = 0, None
for _ in range(n):
    t = int(input())
    if s is not None:
        res += t - s
        s = None
    else:
        s = t
res = res if s is None else "still running"
print(res)
