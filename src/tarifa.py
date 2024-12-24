x, n = (int(input()) for _ in range(2))
p = (int(input()) for _ in range(n))
res = x * (n + 1) - sum(p)
print(res)
