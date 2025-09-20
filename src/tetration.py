from math import pow


# a^n = n -> a = sqrt-n(a)
n = float(input())
res = pow(n, 1/n)
print(res)
