from collections import defaultdict


while True:
    n = int(input())
    if n < 0:
        break
    adj = defaultdict(set)
    for i in range(n):
        a = (int(i) for i in input().split())
        for j, v in enumerate(a):
            if v == 1:
                adj[i].add(j)
                adj[j].add(i)
    res = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if j in adj[i]:
                for v in adj[i] & adj[j]:
                    res.add(v)
    res = sorted(set(range(n)) - res)
    print(*res)
