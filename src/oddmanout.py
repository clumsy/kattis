n = int(input())
for i in range(n):
    g = int(input())
    c = (int(i) for i in input().split())
    res = 0
    for ci in c:
        res ^= ci
    res = f"Case #{i + 1}: {res}"
    print(res)
