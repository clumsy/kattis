e, f, c = (int(i) for i in input().split())
res = 0
e += f
while e >= c:
    res += 1
    e = e - c + 1
print(res)
