def step(x_, y_, dx, dy, d):
    if d == "Left":
        dx, dy = -dy, dx
    elif d == "Right":
        dx, dy = dy, -dx
    else:
        x_ += dx
        y_ += dy
    return x_, y_, dx, dy


x, y = (int(i) for i in input().split())
n = int(input())
ds = [input() for _ in range(n)]


def solve(x_, y_, dx, dy, d, b):
    x_, y_, dx, dy = step(x_, y_, dx, dy, d)
    for i in range(b, n):
        x_, y_, dx, dy = step(x_, y_, dx, dy, ds[i])
    return x_ == x and y_ == y


x_, y_, dx, dy = 0, 0, 0, 1
res = None
for i in range(n):
    if res:
        break
    for d in {"Forward", "Left", "Right"} - set(ds[i]):
        if solve(x_, y_, dx, dy, d, i + 1):
            res = f"{i + 1} {d}"
            break
    x_, y_, dx, dy = step(x_, y_, dx, dy, ds[i])
print(res)
