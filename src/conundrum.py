s = input()
res = 0
for i in range(0, len(s), 3):
    res += s[i + 0] != "P"
    res += s[i + 1] != "E"
    res += s[i + 2] != "R"
print(res)
