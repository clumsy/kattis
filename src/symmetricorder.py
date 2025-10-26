s = 0
while True:
    n = int(input())
    s += 1
    if not n:
        break
    ss = (input() for _ in range(n))
    frt, bck = [], []
    for i, e in enumerate(ss):
        (frt if i & 1 == 0 else bck).append(e)
    res = frt + bck[::-1]
    print("SET", s)
    print(*res, sep="\n")
