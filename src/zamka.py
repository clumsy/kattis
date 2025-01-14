l, d, x = (int(input()) for _ in range(3))
res = [float("inf"), float("-inf")]
for i in range(l, d + 1):
    if sum(int(c) for c in str(i)) == x:
        res[0] = min(res[0], i)
        res[1] = max(res[1], i)
print(*res, sep="\n")
