n, a = int(input()), (int(i) for i in input().split())
res = prv = 0
for i in a:
    if i > prv:
        res += 1
    prv = i
print(res)
