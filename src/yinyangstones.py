s = input()
b = s.count("B")
w = len(s) - b
res = 1 if w == b else 0
print(res)
