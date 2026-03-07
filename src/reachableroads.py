class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
            return True
        return False

for _ in range(int(input())):
    n, m = int(input()), int(input())
    dsu = DSU(n)
    for _ in range(m):
        r = list(map(int, input().split()))
        for i in range(1, len(r)):
            dsu.union(r[0], r[i])
    print(len(set(dsu.find(i) for i in range(n))) - 1)
