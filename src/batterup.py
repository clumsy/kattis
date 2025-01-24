n = int(input())
a = (int(i) for i in input().split())
s = 0
for i in a:
    s += max(0, i)
    n -= i < 0
res = s / n
print(res)
