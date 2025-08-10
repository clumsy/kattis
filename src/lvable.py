n, s = int(input()), input()
res = 2
for i in range(n):
    if s[i] == "l":
        res = 1
    elif s[i] == "v":
        if i and s[i - 1] == "l":
            res = 0
            break
        else:
            res = 1
print(res)
