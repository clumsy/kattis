n = int(input())
a = sorted([int(i) for i in input().split()])
res = a[n // 3: 2 * n // 3] + a[: n // 3] + a[2 * n // 3:]
print(*res)
