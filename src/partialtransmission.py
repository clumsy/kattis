n, p = (int(input()) for _ in range(2))
a = (int(i) for i in input().split())
res = p
for i in range(n - 1):
    res ^= i + 1 + p
for i in a:
    res ^= i
print(res)
