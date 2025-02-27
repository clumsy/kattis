from math import cos, sin, radians

G = 9.81
n = int(input())
for _ in range(n):
    v0, O, x1, h1, h2 = (float(f) for f in input().split())
    O = radians(O)
    t = x1 / (v0 * cos(O))
    y = v0 * t * sin(O) - G * (t ** 2) / 2
    res = "Safe" if h1 + 1 <= y <= h2 - 1 else "Not Safe"
    print(res)
