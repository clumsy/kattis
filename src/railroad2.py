x, y = (int(i) for i in input().split())
res = "possible" if y & 1 == 0 else "impossible"
print(res)
