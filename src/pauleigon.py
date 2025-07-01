n, p, q = (int(i) for i in input().split())
res = "paul" if (p + q) // n & 1 == 0 else "opponent"
print(res)
