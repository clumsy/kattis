m = "Úllen dúllen doff kikke lane koff koffe lane bikke bane úllen dúllen doff.".split()
n, s = int(input()), input().split()
res = s[(len(m) - 1) % len(s)]
print(res)
