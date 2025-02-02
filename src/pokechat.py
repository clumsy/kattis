s, l = (input() for _ in range(2))
res = "".join(s[int(l[i:i + 3].lstrip("0")) - 1] for i in range(0, len(l), 3))
print(res)
