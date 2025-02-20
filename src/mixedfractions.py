while True:
    x, y = (int(i) for i in input().split())
    if x == 0 and y == 0:
        break
    res = " ".join(str(i) for i in divmod(x, y)) + f" / {y}"
    print(res)
