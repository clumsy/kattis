p = int(input())
for _ in range(p):
    k, n = (int(i) for i in input().split())
    res = [
        ((1 + n) * n) // 2,
        ((1 + 2 * n - 1) * n) // 2,
        ((2 + 2 * n) * n) // 2,
    ]
    print(k, *res)
