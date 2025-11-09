s = input()
res = []
for c in s:
    if c in "aeoiu":
        res.append(c)
    elif c == "-":
        res.append("\n")
    elif c in "0123456789":
        res.append(bin(int(c))[2:])
    else:
        res.append("beepbloop")
res = "".join(res)
print(res)
