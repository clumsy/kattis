s = input()
n, res = len(s), []
for i in range(n // 3):
    if s[i] == s[i + n // 3]:
        res.append(s[i])
    elif s[i] == s[i + 2 * n // 3]:
        res.append(s[i])
    elif s[i + n // 3] == s[i + 2 * n // 3]:
        res.append(s[i + n // 3])
res = "".join(res)
print(res)
