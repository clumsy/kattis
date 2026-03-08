a, b = (int(input()) for _ in range(2))
if a <= b:
    d1, d2 = b - a, a + 360 - b
else:
    d1, d2 = (b + 360 - a), a - b
res = d1 if d1 <= d2 else -d2
print(res)
