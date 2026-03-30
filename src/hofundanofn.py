s = input().strip().split()
if len(s) == 1:
    res = s[0]
else:
    res = ", ".join((s[-1], " ".join(f"{c[0].upper()}." for c in s[:-1])))
print(res)
