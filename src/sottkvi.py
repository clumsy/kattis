n, k, d = (int(i) for i in input().split())
res, b = 0, k + d
for _ in range(n):
    i = int(input())
    res += b - i >= 14
print(res)
