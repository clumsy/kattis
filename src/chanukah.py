p = int(input())
for _ in range(p):
    k, n = (int(i) for i in input().split())
    res = k, (1 + n) * n // 2 + n
    print(*res)
