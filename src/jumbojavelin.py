n = int(input())
l = (int(input()) for _ in range(n))
res = sum(l) - (n - 1)
print(res)
