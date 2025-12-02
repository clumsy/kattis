from math import lcm


p, q, s = (int(i) for i in input().split())
res = "yes" if lcm(p, q) <= s else "no"
print(res)
