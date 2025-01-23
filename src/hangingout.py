l, x = (int(i) for i in input().split())
res = cur = 0
for _ in range(x):
    e, p = input().split()
    p = int(p)
    if e == "leave":
        cur = max(0, cur - p)
    elif cur + p <= l:
        cur += p
    else:
        res += 1
print(res)
