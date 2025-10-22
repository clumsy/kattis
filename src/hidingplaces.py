from math import inf
from itertools import product
from collections import defaultdict, deque


t = int(input())
for _ in range(t):
    p = input()
    b = [[inf] * 8 for _ in range(8)]
    r, c = ord(p[0]) - ord("a"), ord(p[1]) - ord("1")
    b[r][c] = cur = 0
    q = deque([(r, c)])
    while q:
        cur += 1
        for _ in range(len(q)):
            r, c = q.pop()
            for dr, dc in product([-2, -1, 1, 2], [-2, -1, 1, 2]):
                r_, c_ = r + dr, c + dc
                if abs(dr) != abs(dc) and 0 <= r_ < 8 and 0 <= c_ < 8 and cur < b[r_][c_]:
                    b[r_][c_] = cur
                    q.appendleft((r_, c_))
    cnt = defaultdict(list)
    for r in range(8):
        for c in range(8):
            cnt[b[r][c]].append("abcdefgh"[r] + "12345678"[c])
    ma = max(cnt.keys())
    res = ma, *sorted(cnt[ma], key=lambda x: (-int(x[1]), x[0]))
    print(*res)
