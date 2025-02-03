s = input()
a = u = False
for i, c in enumerate(s):
    if a and u:
        break
    if i and s[i - 1] == ":":
        a |= c == ")"
        u |= c == "("
res = "double agent" if a and u else "alive" if a and not u else "undead" if not a and u else "machine"
print(res)
