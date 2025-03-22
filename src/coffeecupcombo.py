n = int(input())
s = input()
res = 0
for i, c in enumerate(s):
    res += c == "1" or (i > 0 and s[i - 1] == "1") or (i > 1 and s[i - 2] == "1")
print(res)
