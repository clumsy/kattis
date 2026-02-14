n = int(input())
pa = pb = -1
res = "yes"
for _ in range(n):
    a, b = (int(i) for i in input().split())
    if a < pa or b < pb:
        res = "no"
    pa, pb = a, b
print(res)
