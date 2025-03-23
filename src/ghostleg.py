n, m = (int(i) for i in input().split())
rs = [int(input()) for _ in range(m)]
res = [0] * n
for i in range(n):
    j = i = i + 1
    for r in rs:
        if j == r:
            j += 1
        elif j - r == 1:
            j -= 1
    res[j - 1] = i
print(*res, sep="\n")
