n, q = (int(i) for i in input().split())
d = {}
for _ in range(n):
    s = input()
    name = "".join(c[0] for c in s.split())
    d[name] = "ambiguous" if name in d else s
for _ in range(q):
    res = d.get(input(), "nobody")
    print(res)
