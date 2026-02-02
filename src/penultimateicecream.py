n = int(input())
a = (int(i) for i in input().split())
ma, res = next(a), 0
for i in a:
    if i >= ma:
        ma, res = i, ma
    elif i > res:
        res = i
print(res)
