n = int(input())
s = sorted(-float(input().split()[1]) for i in range(n))
res = sum(-x * (i + 1) for i, x in enumerate(s))
print(res)
