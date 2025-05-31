n = int(input())
res = 0
for _ in range(n):
    t, a = (int(i) for i in input().split())
    if t == 0:
        res += a
    else:
        res = max(0, res - a)
print(res)
