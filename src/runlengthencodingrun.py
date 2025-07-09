t, s = input().split()
s += "#"
if t == "E":
    res, cnt = [], 1
    for i, c in enumerate(s):
        if c == s[i - 1]:
            cnt += 1
        elif i > 0:
            res.append(s[i - 1] + str(cnt))
            cnt = 1
else:
    res, p = [], -1
    for i, c in enumerate(s):
        if not c.isdigit():
            if p >= 0:
                res[-1] = res[-1] * int(s[p:i])
            if i < len(s) - 1:
                p = i + 1
                res.append(c)
res = "".join(res)
print(res)
