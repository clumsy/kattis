n = int(input())
res = sum("CD" not in input() for _ in range(n))
print(res)
