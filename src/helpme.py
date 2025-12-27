from collections import defaultdict


ps = [defaultdict(list) for _ in range(2)]
input()
for r in range(8):
    s = input()[1:].split("|")
    for c, p in zip("abcdefgh", s):
        if p and p[1] not in ".:":
            ps[0 if p[1].isupper() else 1][p[1].upper()].append(f"{c}{8 - r}")
    input()
res = []
for c in range(2):
    r = []
    for t in ("K", "Q", "R", "B", "N", "P"):
        if ps[c][t]:
            r.append(
                ",".join(
                    f"{'' if t == 'P' else t}{v}"
                    for v in sorted(ps[c][t], key=lambda s: ((1 if c == 0 else -1) * int(s[1]), s[0]))
                )
            )
    c = "White" if c == 0 else "Black"
    res.append(f"{c}: {','.join(r)}")
res = "\n".join(res)
print(res)
