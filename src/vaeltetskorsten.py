n = int(input())
res = 0
for _ in range(n):
    d, s = input().split()
    if s == "nej":
        res = max(res, int(d))
print(res)
