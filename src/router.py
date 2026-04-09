n = int(input())
mi_x = ma_x = mi_y = ma_y = x = y = 0
for _ in range(n):
    d, s = input().split()
    s = int(s)
    if d == "U":
        y += s
    elif d == "R":
        x += s
    elif d == "L":
        x -= s
    else:
        y -= s
    mi_x, ma_x = min(mi_x, x), max(ma_x, x)
    mi_y, ma_y = min(mi_y, y), max(ma_y, y)
res = 40 + (ma_x - mi_x), 40 + (ma_y - mi_y)
print(*res)
