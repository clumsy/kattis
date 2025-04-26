w, p = (int(i) for i in input().split())
res = "YES" if 180 * p >= (w + 1) // 2 else "NO"
print(res)
