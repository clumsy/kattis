s = int(input())
m, s = divmod(s, 60)
h, m = divmod(m, 60)
res = " : ".join(str(i) for i in (h, m, s))
print(res)
