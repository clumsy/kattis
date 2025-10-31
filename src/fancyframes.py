a, b, c, d = input().split()
c, d = int(c), int(d)
n = 2 * (c + d) + len(a)
res = [
    *(b * n for _ in range(c)),
    *(b * c + " " * (n - 2 * c) + b * c for _ in range(d)),
    b * c + " " * d + a + " " * d + b * c,
    *(b * c + " " * (n - 2 * c) + b * c for _ in range(d)),
    *(b * n for _ in range(c)),
]
print(*res, sep="\n")
