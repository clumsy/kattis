a, b, c = (int(input()) for _ in range(3))
# 2 * a * x + b = 0 => x = -b / (2 * a)
# x = -b / (2 * a)
# f_x = a * x ** 2 + b * x + c
# f_x = (b * b) / (4 * a) + (b * -b) / (2 * a) + c
f_x = (-b * b) / (4 * a) + c
res = 1 if f_x == 0 else 2 if (a > 0) != (f_x > 0) else 0
print(res)
