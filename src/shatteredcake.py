w = int(input())
n = int(input())
res = 0
for _ in range(n):
    wi, li = (int(i) for i in input().split())
    res += wi * li
res = res // w
print(res)
