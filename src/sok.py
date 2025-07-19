a, b, c = (int(i) for i in input().split())
i, j, k = (int(i) for i in input().split())
x = min(u / d for u, d in zip((a, b, c), (i, j, k)))
res = a - x * i, b - x * j, c - x * k
print(*res)
