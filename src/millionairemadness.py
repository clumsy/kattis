from heapq import heappop, heappush


m, n = (int(i) for i in input().split())
v = [[int(i) for i in input().split()] for _ in range(m)]
lad = [[float("inf")] * n for _ in range(m)]
q = [(0, 0, 0)]
while True:
    res, r, c = heappop(q)
    if r == m - 1 and c == n - 1:
        break
    for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        r_, c_ = r + dr, c + dc
        if 0 <= r_ < m and 0 <= c_ < n:
            res_ = max(res, v[r_][c_] - v[r][c])
            if res_ < lad[r_][c_]:
                lad[r_][c_] = res_
                heappush(q, (res_, r_, c_))
print(res)
