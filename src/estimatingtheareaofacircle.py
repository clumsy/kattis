from math import pi


while True:
    r, m, c = input().split()
    if r == m == c == "0":
        break
    r, m, c = float(r), int(m), int(c)
    res = [pi * r * r, 4 * r * r * (c / m)]
    print(*res)
