from functools import reduce
from operator import xor

n = int(input())
x = (int(i) for i in input().split())
y = (int(i) for i in input().split())
res = reduce(xor, x) ^ reduce(xor, y)
print(res)
