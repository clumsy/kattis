# n = int(input())
# cs = [sorted(input().split()[1:]) for _ in range(n)]
# res = []


# def dfs(cur, d=0):
#     if d == n:
#         res.append(" ".join(cur))
#         return
#     for p in cs[d]:
#         cur.append(p)
#         dfs(cur, d + 1)
#         cur.pop()


# dfs([])
# print(*res, sep="\n")

import itertools

n = int(input())
cs = [sorted(input().split()[1:]) for _ in range(n)]

res = (" ".join(combo) for combo in itertools.product(*cs))
print(*res, sep="\n")
