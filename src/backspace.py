s = input()
res = []
for c in s:
    if c == "<" and s:
        res.pop()
    else:
        res.append(c)
res = "".join(res)
print(res)
