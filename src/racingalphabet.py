from math import pi
from string import ascii_uppercase


a = ascii_uppercase + " '"
n = int(input())
for _ in range(n):
    s = input()
    res, cur = 0, a.find(s[0])
    for c in s:
        nxt = a.find(c)
        d = abs(cur - nxt)
        res += min(d, len(a) - d)
        cur = nxt
    res = pi * 60 * (res / len(a)) / 15 + len(s)
    print(res)
