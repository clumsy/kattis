s = input()
t = h = 0
for c in s:
    t += c == "T"
    h += c == "H"
    if max(t, h) > 10 and max(t, h) - min(t, h) > 1:
        t = h = 0
res = f"{t}-{h}"
print(res)
