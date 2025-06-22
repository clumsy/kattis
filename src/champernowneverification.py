n = input()
res = o = 0
while res >= 0 and o < len(n):
    res += 1
    for ci, ni in zip(str(res), n[o:]):
        if ci != ni:
            res = -1
            break
        o += 1
print(res)
