a, b = input().split()
res = int(max(a[::-1], b[::-1]))
print(res)
