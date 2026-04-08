f = input()
bgd = (int(input()) for i in range(3))
fgd = (int(input()) for i in range(3))


def diff(x, y, t):
    return sum(abs(xi - yi) for xi, yi in zip(x, y)) <= t


res = "L33T H4X0R" if (f == "monospace") + diff(bgd, (0, 0, 0), 25) + diff(fgd, (0, 255, 0), 35) >= 2 else "n00b"
print(res)
