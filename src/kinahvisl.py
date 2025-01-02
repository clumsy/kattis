s, t = (input() for _ in range(2))
res = 1 + sum(si != ti for si, ti in zip(s, t))
print(res)
