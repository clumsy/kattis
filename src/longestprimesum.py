n = input()
res = r = 0
for d in n:
    d, r = divmod(r * 10 + int(d), 2)
    res = res * 10 + d
print(res)
