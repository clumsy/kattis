n, m = (int(i) for i in input().split())
res = None
for _ in range(n):
    s = input().split()
    res = res & set(s) if res is not None else set(s)
res = sorted(res)
print(len(res))
print(*res, sep="\n")
