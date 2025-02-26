a, b = (int(i) for i in input().split())
a, b = (b, a) if a < b else (a, b)
while b > 0:
    a, b = b, a % b
res = a
print(res)
