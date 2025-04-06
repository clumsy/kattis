s = input()
res = []
for i in range(1, len(s)):
    if s[i] == ")":
        if s[i - 1] in ":;":
            res.append(i - 1)
        elif s[i - 1] == "-" and s[i - 2] in ":;":
            res.append(i - 2)
print(*res, sep="\n")
