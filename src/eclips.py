s = input().split()
res = (c for c in s if "e" in c)
res = next(res, "oh noes"), *res
print(*res)
