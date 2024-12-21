n = float(input())
d = n % 1
res = int(n - d) + (d >= 0.5)
print(res)
