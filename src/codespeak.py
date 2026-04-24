n = int(input())
s = input()
res, ib = [], False
for c in s[::-1] + "#":
    if c in "aioeu":
        ib = True
    elif ib:
        res.append("ib")
        ib = False
    res.append(c)
res = "".join(res[-2::-1])
print(res)
