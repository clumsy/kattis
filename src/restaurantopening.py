# n, m = (int(i) for i in input().split())
# g = [[int(i) for i in input().split()] for _ in range(n)]
# res = float("inf")
# for r0 in range(n):
#     for c0 in range(m):
#         cur = 0
#         for r in range(n):
#             for c in range(m):
#                 cur += g[r][c] * (abs(r - r0) + abs(c - c0))
#         res = min(res, cur)
# print(res)

n, m = (int(i) for i in input().split())
g = [list(map(int, input().split())) for _ in range(n)]

total_people = sum(sum(row) for row in g)


def weighted_median(weights_iter):
    half = total_people / 2
    cum = 0
    for i, w in enumerate(weights_iter):
        cum += w
        if cum >= half:
            return i


r0 = weighted_median(sum(row) for row in g)
c0 = weighted_median(sum(g[r][c] for r in range(n)) for c in range(m))

res = 0
for r in range(n):
    for c in range(m):
        res += g[r][c] * (abs(r - r0) + abs(c - c0))

print(res)
