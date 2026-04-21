n = int(input())
a = b = 0
for _ in range(n):
    m, s = (int(i) for i in input().split())
    a += m * 60
    b += s
res = b / a
res = res if res > 1 else "measurement error"
print(res)
