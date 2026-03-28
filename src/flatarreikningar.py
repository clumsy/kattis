from math import pi, pow


v = float(input())
# v = 4 * pi * r^3/3 => r = pow(3 * v / (4 * pi), 1./3)
# a = 4 * pi * r ^ 2
res = 0 if v == 0 else 4 * pi * (pow(3 * v / (4 * pi), 1.0 / 3)) ** 2
print(res)
