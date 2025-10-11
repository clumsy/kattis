a, b, c, n = (int(i) for i in input().split())
res = "YES" if n > 2 and min(a, b, c) > 0 and a + b + c >= n else "NO"
print(res)
