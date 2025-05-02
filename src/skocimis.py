a, b, c = (int(i) for i in input().split())
res = max(0, c - b - 1, b - a - 1)
print(res)
