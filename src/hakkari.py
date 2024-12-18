n, m = (int(i) for i in input().split())
res = []
for r in range(n):
    s = input()
    for c in range(m):
        if s[c] == "*":
            res.append((r + 1, c + 1))
print(len(res))
for r in res:
    print(*r)
