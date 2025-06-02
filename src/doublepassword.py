import operator
from functools import reduce


a, b = (input() for _ in range(2))
res = reduce(operator.mul, (1 if ai == bi else 2 for ai, bi in zip(a, b)))
print(res)
