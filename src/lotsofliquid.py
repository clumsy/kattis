from math import cbrt


n, a = int(input()), (float(i) for i in input().split())
res = cbrt(sum(x**3 for x in a))
print(res)
