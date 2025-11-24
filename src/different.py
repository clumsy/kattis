while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    if len(b) > len(a) or (len(a) == len(b) and b > a):
        a, b = b, a
    a, b = ([int(i) for i in s] for s in (a, b))
    res, c = [], 0
    while a or b:
        i, j = a.pop() if a else 0, b.pop() if b else 0
        c = i - j + c
        c, v = (-1, 10 + c) if c < 0 else (0, c)
        res.append(v)
    while len(res) > 1 and not res[-1]:
        res.pop()
    res = "".join(str(i) for i in res)[::-1]
    print(res)
