while True:
    n = int(input())
    if not n:
        break
    a = [int(input()) for _ in range(n)]
    b = (int(input()) for _ in range(n))
    m = dict(zip(sorted(a), sorted(b)))
    res = (m[i] for i in a)
    print(*res, sep="\n")
    print()
