n, c, p = (int(i) for i in input().split())
res = 0
for _ in range(n):
    x = int(input())
    if x > c + p:
        res += 1
        c, p = x, c
print(res)
