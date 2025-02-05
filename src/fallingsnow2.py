n, m = (int(i) for i in input().split())
cnt = [0] * m
for _ in range(n):
    for i, c in enumerate(input()):
        cnt[i] += c == "S"
for i in range(n):
    res = "".join("S" if n - i <= c else "." for c in cnt)
    print(res)
