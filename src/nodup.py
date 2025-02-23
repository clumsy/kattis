s = input().split()
unq = set()
res = "yes"
for c in s:
    if c in unq:
        res = "no"
    unq.add(c)
print(res)
