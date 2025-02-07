n = int(input())
ws = input().split()
m = int(input())
d = {}
for _ in range(m):
    a, b = input().split()
    d[a] = b
res = " ".join(d[w] for w in ws)
print(res)
