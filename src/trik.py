s = input()
res = [1, 0, 0]
for c in s:
    if c == "A":
        res[0], res[1] = res[1], res[0]
    elif c == "B":
        res[1], res[2] = res[2], res[1]
    elif c == "C":
        res[0], res[2] = res[2], res[0]
res = next(i + 1 for i, e in enumerate(res) if e == 1)
print(res)
