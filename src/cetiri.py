a, b, c = sorted(int(i) for i in input().split())
d = min(b - a, c - b)
missing = set(a + i * d for i in range(4)) - {a, b, c}
res = next(iter(missing), a)
print(res)
