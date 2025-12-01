n, p = (int(i) for i in input().split())
ps = [None] * p
for i in range(p):
    _, *a = (int(i) for i in input().split())
    ps[i] = list(a)
m = int(input())
for _ in range(m):
    s, d, n = (int(i) for i in input().split())
    ps[d - 1].extend(ps[s - 1][-n:])
    del ps[s - 1][-n:]
for res in ps:
    print(*res)
