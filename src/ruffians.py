from collections import defaultdict


t = int(input())
for _ in range(t):
    s1 = (int(i) for i in input().split())
    s2 = (int(i) for i in input().split())
    m1 = defaultdict(set)
    for i, v in enumerate(s1):
        m1[v].add(i)
    res = "NO"
    for i, v in enumerate(s2):
        was = i in m1[v]
        if was:
            m1[v].remove(i)
        if len(m1[v]) > 0:
            res = "YES"
            break
        if was:
            m1[v].add(i)
    print(res)
