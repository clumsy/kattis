from bisect import bisect


t = int(input())
for _ in range(t):
    a = [int(i) for i in input().split()]
    idx, a, q, res = a[0], a[1:], [], 0
    for i in a:
        p = bisect(q, i)
        res += len(q) - p
        q = q[:p] + [i] + q[p:]
    res = idx, res
    print(*res)
