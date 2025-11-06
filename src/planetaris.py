n, a = (int(i) for i in input().split())
e = (int(i) for i in input().split())
res = 0
for i in sorted(e):
    if a <= i:
        break
    a -= i + 1
    res += 1
print(res)
