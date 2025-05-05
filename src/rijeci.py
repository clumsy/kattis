k = int(input())
a, b = 1, 0
while k:
    a, b = b, b + a
    k -= 1
res = a, b
print(*res)
