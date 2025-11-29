n, m = (int(i) for i in input().split())
d1 = [int(i) for i in input().split()]
d2 = [int(i) for i in input().split()]
res = [
    " ".join(str(i) for i in d1 if i not in set(d2)),
    " ".join(str(i) for i in d2 if i not in set(d1)),
]
print(*res, sep="\n")
