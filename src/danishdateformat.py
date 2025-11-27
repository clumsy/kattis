s = input()
m, d, y = (int(i.lstrip("0") or 0) for i in s.split("/"))
m = "januar februar marts april maj juni juli august september oktober november december".split()[m - 1]
res = f"{d}. {m} {y}"
print(res)
