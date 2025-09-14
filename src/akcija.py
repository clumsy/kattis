n = int(input())
a = [int(input()) for _ in range(n)]
a = sorted(a, reverse=True)
res = sum(a) - sum(a[2::3])
print(res)
