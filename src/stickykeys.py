s = input()
res = []
for i, c in enumerate(s):
    if i == 0 or c != s[i - 1]:
        res.append(c)
res = "".join(res)
print(res)
