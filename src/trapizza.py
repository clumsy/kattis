from math import pi


d, a, b, h = (int(input()) for _ in range(4))
d = h * (a + b) / 2 - pi * (d / 2) ** 2
res = "Jafn storar!" if d == 0 else "Trapizza!" if d > 0 else "Mahjong!"
print(res)
