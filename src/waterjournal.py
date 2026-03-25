n, mi, ma = (int(i) for i in input().split())
a = (int(input()) for _ in range(n - 1))
has_mi = has_ma = False
for i in a:
    has_mi |= i == mi
    has_ma |= i == ma
res = (
    [-1]
    if not has_mi and not has_ma
    else [mi]
    if not has_mi
    else [ma]
    if not has_ma
    else [i for i in range(mi, ma + 1)]
)
print(*res, sep="\n")
