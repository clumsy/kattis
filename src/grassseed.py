from operator import mul

c, l = (float(input()) for _ in range(2))
w = ((float(i) for i in input().split()) for _ in range(int(l)))
res = c * sum(mul(*wi) for wi in w)
print(res)
