n, s = int(input()), input().split()
res = "".join(c[0] for c in s if "A" <= c[0] <= "Z")
print(res)
