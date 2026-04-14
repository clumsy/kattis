r, f = (int(i) for i in input().split())
res = "up" if ((f + (r + 1) // 2) // r) & 1 == 0 else "down"
print(res)
