s = input()
res = []
for c in s:
    if not res or c != res[-1]:
        res.append(c)
res = "".join(res)
print(res)
