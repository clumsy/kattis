n = int(input())
res, ma = None, 0
for _ in range(n):
    s, c, f = input().split()
    cur = int(c) * int(f)
    if res is None or cur > ma:
        res = s
        ma = cur
    elif cur == ma:
        res = min(res, s)
print(res)
