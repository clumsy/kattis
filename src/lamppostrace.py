n, a = int(input()), (int(i) for i in input().split())
res = p = next(a)
for i in a:
    res += abs(i - p)
    p = i
print(res)
