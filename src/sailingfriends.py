# n, b, m = (int(i) for i in input().split())
# bs = (int(i) for i in input().split())


# class UnionFind:
#     def __init__(self, n):
#         self.prnt = list(range(n))
#         self.sz = [1] * n

#     def find(self, i):
#         while self.prnt[i] != i:
#             self.prnt[i] = self.prnt[self.prnt[i]]
#             i = self.prnt[i]
#         return i

#     def union(self, a, b):
#         ra, rb = self.find(a), self.find(b)

#         if ra == rb:
#             return

#         if self.sz[ra] < self.sz[rb]:
#             ra, rb = rb, ra

#         self.prnt[rb] = ra
#         self.sz[ra] += self.sz[rb]


# uf = UnionFind(n)
# for _ in range(m):
#     f, s = (int(i) for i in input().split())
#     uf.union(f - 1, s - 1)
# res = sum(uf.find(i) == i for i in range(n)) - len(set(uf.find(i - 1) for i in bs))
# print(res)

from collections import defaultdict


n, b, m = (int(i) for i in input().split())
bs = set(int(i) for i in input().split())
adj = defaultdict(list)
for _ in range(m):
    f, s = (int(i) for i in input().split())
    adj[f].append(s)
    adj[s].append(f)
seen = set()
res = 0
for i in range(n):
    i += 1
    if i in seen:
        continue
    seen.add(i)
    st = [i]
    boat = False
    while st:
        c = st.pop()
        boat |= c in bs
        for p in adj[c]:
            if p not in seen:
                seen.add(p)
                st.append(p)
    res += not boat
print(res)
