from math import sin, sqrt, acos, pi


while True:
    try:
        r, x, y = (float(i) for i in input().split())
        if x * x + y * y >= r * r:
            res = ["miss"]
        else:
            h2 = x * x + y * y
            s2 = 4 * (r * r - h2)
            q = acos(1 - s2/(2 * r * r))
            res = r * r / 2 * (q - sin(q))
            res = pi * r * r - res, res
        print(*res)
    except EOFError:
        break
