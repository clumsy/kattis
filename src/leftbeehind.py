while True:
    x, y = (int(i) for i in input().split())
    if x == y == 0:
        break
    res = "Never speak again." if x + y == 13 else "Undecided." if x == y else "Left beehind." if y > x else "To the convention."
    print(res)
