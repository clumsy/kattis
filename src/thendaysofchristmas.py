n = int(input())
res = cur = 0
for i in range(1, n + 1):
    cur += i
    res += cur
res = cur, res
print(*res, sep="\n")
