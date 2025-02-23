unq = {s: set() for s in ("P", "K", "H", "T")}
s = input()
res = None
for i in range(0, len(s), 3):
    c = s[i: i + 3]
    if c in unq[c[0]]:
        res = "GRESKA"
    unq[c[0]].add(c)
res = res if res == "GRESKA" else " ".join(str(13 - len(unq[s])) for s in ("P", "K", "H", "T"))
print(res)
