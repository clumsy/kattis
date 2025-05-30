a, b = (input() for _ in range(2))
res = a.count("S") * b.count("S")
res = "S(" * res + "0" + ")" * res
print(res)
