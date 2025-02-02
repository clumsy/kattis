n, m, k = (int(i) for i in input().split())
res = [["."] * m for _ in range(n)]
for _ in range(k):
    r, c = (int(i) for i in input().split())
    res[r - 1][c - 1] = "*"
for r in res:
    print("".join(r))
