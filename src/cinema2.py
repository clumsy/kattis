n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = m
while a:
    n -= next(a)
    if n < 0:
        break
    res -= 1
print(res)
