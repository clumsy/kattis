n = int(input())
res = (2, -1) if n == 1 else (-2, 1) if n == -1 else (n - 1, 1) if n >= 0 else (n + 1, -1)
print(*res)
