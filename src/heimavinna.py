s = input()
res = 0
for c in s.split(";"):
    if "-" in c:
        c = [int(i) for i in c.split("-")]
        res += c[-1] - c[0] + 1
    else:
        res += 1
print(res)
