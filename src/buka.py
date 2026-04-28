a, o, b = (input() for _ in range(3))
if o == "*":
    res = a + "0" * (len(b) - 1)
else:
    a, b = "0" * max(0, len(b) - len(a)) + a, "0" * max(0, len(a) - len(b)) + b
    res = []
    for x, y in zip(a, b):
        res.append(str(int(x) + int(y)))
    res = "".join(res)
print(res)
