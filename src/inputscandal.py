res = []
try:
    while True:
        s = input()
        res.append(s)
except:
    pass
print(len(res))
print(*res, sep="\n")
