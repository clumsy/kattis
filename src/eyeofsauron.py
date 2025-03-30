s = input()
res = "correct" if 2 * s.find("(") + 2 == len(s) else "fix"
print(res)
