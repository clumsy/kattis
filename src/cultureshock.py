n, s = int(input()), input()
ws = {"he", "she", "him", "her"}
res = sum(c in ws for c in s.split())
print(res)
