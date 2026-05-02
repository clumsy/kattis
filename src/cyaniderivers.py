s = input()
res = max((len(c) + 1) // 2 for c in s.split("1"))
print(res)
