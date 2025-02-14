n, m = (int(input()) for _ in range(2))
d, r = divmod(m, n)
for _ in range(r):
    print("*" * (d + (r > 0)))
for _ in range(n - r):
    print("*" * d)
