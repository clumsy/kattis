s, n = input(), int(input())
res = n
for i in range(n):
    x = input()
    if len(x) == len(s) and sum(cx != cs for cx, cs in zip(x, s)) < 2:
        res = min(res, i + 1)
print(res)
