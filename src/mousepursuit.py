n = int(input())
ss = [input() for _ in range(n)]
k = int(input())
c_ = g_ = 0
for s in ss:
    s = s.split()
    t, s, c, g = s[0], *(int(i) for i in s[1:])
    if s <= k:
        d = 1 if t == "CAUGHT" else -1
        c_ += d * c
        g_ += d * g
res = c_, g_
print(*res)
