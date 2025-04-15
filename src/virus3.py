f, h = (input() for _ in range(2))
i = 0
for c in h:
    if i < len(f) and f[i] == c:
        i += 1
res = "Ja" if i == len(f) else "Nej"
print(res)
