while True:
    a, b, c = sorted(int(i) for i in input().split())
    if a == 0:
        break
    res = "right" if a * a + b * b == c * c else "wrong"
    print(res)
