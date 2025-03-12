n = int(input())
for _ in range(n):
    o = (int(i) for i in input().split())
    k = next(o)
    res = sum(o) - (k - 1)
    print(res)
