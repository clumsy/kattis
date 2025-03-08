x = input()
while len(x) > 1:
    res = 1
    for c in x:
        if c != "0":
            res *= int(c)
    x = str(res)
res = x
print(res)
