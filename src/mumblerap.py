n = int(input())
res, cur = 0, []
s = input()
for c in s:
    if "0" <= c <= "9":
        cur.append(c)
    elif cur:
        res = max(res, int("".join(cur)))
        cur.clear()
else:
    if cur:
        res = max(res, int("".join(cur)))
print(res)
