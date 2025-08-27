n = int(input())
res, i = 0, 1
while i <= n:
    res += (n & i) == i
    i <<= 1
print(res)
