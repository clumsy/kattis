n = int(input())
res = []
for _ in range(n):
    i, k = input().split()
    if not i.isdigit():
        i, k = 2 * int(k), i
    res.append((int(i), k))
res.sort()
res = [k for _, k in res]
print(*res, sep="\n")
