wc, hc, ws, hs = (int(i) for i in input().split())
res = 1 if wc - ws >= 2 and hc - hs >= 2 else 0
print(res)
