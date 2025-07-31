cs = input().split()
cm = {n: i for i, n in enumerate(cs)}
n = int(input())
ss = [input().split() for _ in range(n)]
k = int(input())
ks = [input() for _ in range(k)]
for kn in ks:
    ss.sort(key=lambda x: x[cm[kn]])
    res = [" ".join(s) for s in ss]
    print(*cs)
    print(*res, sep="\n")
    print()
