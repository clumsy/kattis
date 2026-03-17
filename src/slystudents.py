from math import gcd


def base3(i):
    res = []
    while i:
        i, r = divmod(i, 3)
        res.append(r)
    return "".join(str(i) for i in res[::-1])


s = input()
for c in s.split():
    g = gcd(*(ord(i) for i in c))
    res = " ".join(base3(ord(i) // g) for i in c)
    print(g, res, sep="\n")
