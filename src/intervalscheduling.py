n = int(input())
a = (tuple(int(i) for i in input().split()) for _ in range(n))
res = p = 0
for s, f in sorted(a, key=lambda x: x[1]):
    if s >= p:
        res += 1
        p = f
print(res)
