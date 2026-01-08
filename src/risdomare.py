n = int(input())
s = input()
res = sorted(
    (
        (e[0] + e[1], e[0] if s == "antal" else e[1], i + 1)
        for i, e in enumerate(tuple(int(i) for i in input().split()) for _ in range(n))
    ),
    reverse=True,
)[0][-1]
print(res)
