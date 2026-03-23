xs, ys = [0] * 3, [0] * 3
for i in range(3):
    x, y = (int(i) for i in input().split())
    xs[i], ys[i] = x, y
ds = [(xs[i] - xs[i - 1]) ** 2 + (ys[i] - ys[i - 1]) ** 2 for i in range(3)]
a, b = (0, 2) if ds[0] > max(ds[1], ds[2]) else (0, 1) if ds[1] > max(ds[0], ds[2]) else (1, 2)
x0_2, y0_2 = xs[a] + xs[b], ys[a] + ys[b]
c = 3 - (a + b)
# (xs[c] + xs[d]) / 2 = x0 => xs[d] = 2 * x0 - xs[c]
res = x0_2 - xs[c], y0_2 - ys[c]
print(*res)
