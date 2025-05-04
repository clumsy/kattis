s = input()
res = []
for c in s:
    if len(res) > 1 and c in "aeoui" and res[-1] == "p" and res[-2] == c:
        res.pop()
        res.append("")
    else:
        res.append(c)
res = "".join(res)
print(res)
