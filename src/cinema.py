n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = 0
for i in a:
    if i > n:
        res += 1
    else:
        n -= i
print(res)
