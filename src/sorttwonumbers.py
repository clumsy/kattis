a, b = (int(i) for i in input().split())
res = [min(a, b), max(a, b)]
print(*res)
