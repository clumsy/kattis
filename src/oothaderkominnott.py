i = int(input())
d = [int(input()) for _ in range(i)]
w, l, h = (d[0], d[0], 3) if i == 1 else (d[0], d[1], 3) if i == 2 else d
res = (w - 2) * (l - 2) + 2 * h * (w - 1 + l - 1)
print(res)
