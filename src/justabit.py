s = input()
z = s.count("0")
res = z, len(s) - z
print(*res)
