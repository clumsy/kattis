xs, ys = [0] * 3, [0] * 3
for k in range(3):
    xs[k], ys[k] = (int(i) for i in input().split())

def area(ax, ay, bx, by, cx, cy):
    return abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2
a = area(xs[0], ys[0], xs[1], ys[1], xs[2], ys[2])
print(f"{a:.1f}")

n, res = int(input()), 0

# def cross2(sx, sy, ex, ey):
#     return sx * ey - sy * ex
# def cross3(sx, sy, ex, ey, px, py):
#     return cross2(ex - sx, ey - sy, px - sx, py - sy)
# for _ in range(n):
#     px, py = (int(i) for i in input().split())
#     crosses = [cross3(xs[i], ys[i], xs[i + 1], ys[i + 1], px, py) for i in range(-1, 2)]
#     res += all(i >= 0 for i in crosses) or all(i <= 0 for i in crosses)


for _ in range(n):
    px, py = (int(i) for i in input().split())
    res += a == (
        area(xs[0], ys[0], xs[1], ys[1], px, py) +
        area(xs[1], ys[1], xs[2], ys[2], px, py) +
        area(xs[0], ys[0], xs[2], ys[2], px, py)
    )

print(res)
