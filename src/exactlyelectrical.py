a, b = (int(i) for i in input().split())
c, d = (int(i) for i in input().split())
t = int(input())
p = abs(a - c) + abs(b - d)
res = "Y" if t >= p and (p & 1) == (t & 1) else "N"
print(res)
