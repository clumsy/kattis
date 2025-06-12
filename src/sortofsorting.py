while True:
    n = int(input())
    if n == 0:
        break
    res = [input() for _ in range(n)]
    res = [(s[:2], i, s) for i, s in enumerate(res)]
    res = [s for _, _, s in sorted(res)]
    print(*res, sep="\n")
    print()
