r, n = (int(i) for i in input().split())
res = set(range(1, r + 1))
for _ in range(n):
    i = int(input())
    res.remove(i)
res = next(iter(res)) if res else "too late"
print(res)
