from math import isqrt

t = int(input())
for _ in range(t):
    s = input()
    n = isqrt(len(s))
    m = [[None] * n for _ in range(n)]
    for i, c in enumerate(s):
        m[i // n][i % n] = c
    res = "".join(m[r][c] for c in reversed(range(n)) for r in range(n))
    print(res)
