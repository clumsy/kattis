a, b = sorted(int(input()) for _ in range(2))
res = min(b - a, a + 360 - b)
print(res)
