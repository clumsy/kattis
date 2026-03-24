n = int(input())
res, ma = None, 0
for _ in range(n):
    s, p, k = input().split()
    p, k = int(p) + 1, int(k)
    if p * k > ma:
        res = s
        ma = p * k
res = res, ma
print(*res)
