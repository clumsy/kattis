from collections import Counter

w, g = (input() for _ in range(2))
cnt = Counter(w)
res = ["-"] * len(w)
for i, (cw, cg) in enumerate(zip(w, g)):
    if cw == cg:
        if cnt[cw]:
            cnt[cg] -= 1
            res[i] = "G"
for i, (cw, cg) in enumerate(zip(w, g)):
    if res[i] == "-" and cnt[cg] > 0:
        res[i] = "Y"
        cnt[cg] -= 1
res = "".join(res)
print(res)
