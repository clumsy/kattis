k, s = (int(i) for i in input().split())
res = sum(divmod(s, k))
print(res)
