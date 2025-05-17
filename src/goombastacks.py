n = int(input())
res = "possible"
gg = 0
for _ in range(n):
    g, b = (int(i) for i in input().split())
    gg += g
    if gg < b:
        res = "impossible"
print(res)
