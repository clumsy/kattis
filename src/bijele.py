h = (int(i) for i in input().split())
res = (n - h for n, h in zip([1, 1, 2, 2, 2, 8], h))
print(*res)
