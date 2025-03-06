s = input()
a = b = 0
for i in range(0, len(s), 2):
    p, v = s[i:i + 2]
    if p == "A":
        a += int(v)
    else:
        b += int(v)
res = "A" if a >= 11 and a - b >= 2 else "B"
print(res)
