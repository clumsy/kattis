n, k = (int(i) for i in input().split())
rs = (int(input()) for _ in range(k))
s = sum(rs)
res = (s + -3 * (n - k)) / n, (s + 3 * (n - k)) / n
print(*res)
