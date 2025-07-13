wng, rgt = {}, {}
while True:
    s = input()
    if s == "-1":
        break
    m, n, r = s.split()
    if r == "wrong":
        wng[n] = wng.get(n, 0) + 1
    else:
        rgt[n] = int(m)
res = len(rgt), sum(r + wng.get(n, 0) * 20 for n, r in rgt.items())
print(*res)
