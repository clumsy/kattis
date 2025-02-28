n = int(input())
res = 3
for _ in range(1, n):
    res = 2 * res - 1
res = res ** 2
print(res)
