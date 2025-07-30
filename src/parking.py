from heapq import heappop, heappush


a, b, c = (int(i) for i in input().split())
q = []
for i in range(3):
    s, e = (int(i) for i in input().split())
    heappush(q, (s, 1))
    heappush(q, (e, -1))
res = cur = o = 0
p = [0, a, 2 * b, 3 * c]
while q:
    t, i = heappop(q)
    if o:
        res += p[cur] * (t - o)
    cur += i
    o = t
print(res)
