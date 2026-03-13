b, d, c, l = (int(i) for i in input().split())
res = []
for i in range(l // b + 1):
    for j in range((l - i * b) // d + 1):
        for k in range((l - i * b - j * d) // c + 1):
            if i * b + j * d + k * c == l:
                res.append(f"{i} {j} {k}")
res = res or ["impossible"]
print(*res, sep="\n")
