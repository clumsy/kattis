n = int(input())
if n == 0:
    res = "{}"
elif n == 1:
    res = "{{}}"
else:
    res = "{{}}"
    while n > 1:
        n -= 1
        res = res[:-1] + "," + res + "}"
print(res)
