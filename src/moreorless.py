while True:
    a, b = (int(i) for i in input().split())
    if a == b:
        break
    res = "More" if a > b else "Less"
    print(res)
