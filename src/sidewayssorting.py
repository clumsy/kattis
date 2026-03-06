while True:
    r, c = (int(i) for i in input().split())
    if r == c == 0:
        break
    s = [input() for _ in range(r)]
    ss = sorted(["".join(s[i][j] for i in range(r)) for j in range(c)], key=lambda x: x.lower())
    res = ["".join(ss[i][j] for i in range(c)) for j in range(r)]
    print(*res, sep="\n")
    print()
