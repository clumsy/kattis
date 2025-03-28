n = int(input())
res = [2] * (n // 2)
if n & 1 == 1:
    res[0] += 1
print(len(res))
print(*res)
