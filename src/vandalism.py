s = input()
s = set(s)
res = "".join(c for c in "UAPC" if c not in s)
print(res)
