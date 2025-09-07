n = int(input())
res = 0
for k in range(n):
    res += sum(range(1, k)) ** 2 == sum(i ** 3 for i in range(1, k))
print(res)
