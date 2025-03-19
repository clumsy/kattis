l, r = (int(i) for i in input().split())
res = "fits" if 2 * r ** 2 >= l ** 2 else "nope"
print(res)
