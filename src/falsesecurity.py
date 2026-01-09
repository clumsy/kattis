c2m = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ".": "---.",
    ",": ".-.-",
    "?": "----",
}
m2c = {m: c for c, m in c2m.items()}
try:
    while True:
        s = input()
        rs, ls = [], []
        for c in s:
            rs.append(c2m[c])
            ls.append(len(c2m[c]))
        res = []
        cur = 0
        rs = "".join(rs)
        for l in ls[::-1]:
            res.append(m2c[rs[cur : cur + l]])
            cur += l
        res = "".join(res)
        print(res)
except EOFError:
    pass
