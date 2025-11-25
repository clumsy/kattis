n = int(input())
res, m = [], 0
for _ in range(n):
    s = input()
    if s == "/":
        x = m
    else:
        x = int(s)
        m = max(m, ((x + 10) // 10) * 10)
    res.append(x)
print(*res, sep="\n")
