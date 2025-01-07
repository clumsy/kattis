h, m = (int(i) for i in input().split())
h = h if m > 45 else (h - 1) % 24
m = (m - 45) % 60
res = h, m
print(*res)
