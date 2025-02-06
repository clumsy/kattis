n = int(input())
mi, ma = -float("inf"), float("inf")
for _ in range(n):
    a, b = (int(i) for i in input().split())
    mi = max(mi, a)
    ma = min(ma, b)
res = "bad news" if mi > ma else f"{ma - mi + 1} {mi}"
print(res)
