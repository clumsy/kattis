from functools import reduce
from operator import mul


a, b = (int(i) for i in input().split())
sa = sum(reduce(mul, (int(i) for i in input().split())) for _ in range(a))
sb = sum(reduce(mul, (int(i) for i in input().split())) for _ in range(b))
res = "same" if sa == sb else "different"
print(res)
