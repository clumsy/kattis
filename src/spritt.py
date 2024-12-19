n, x = (int(i) for i in input().split())
a = (int(input()) for _ in range(n))
res = "Jebb" if x >= sum(a) else "Neibb"
print(res)
