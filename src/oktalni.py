m = {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7,
}
s = input()
res = []
while s:
    if len(s) < 3:
        s = "0" * (3 - len(s)) + s
    res.append(m[s[-3:]])
    s = s[:-3]
res = "".join(str(i) for i in res[::-1])
print(res)
