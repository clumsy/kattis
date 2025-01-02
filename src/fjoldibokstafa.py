s = input()
any_uc = any_lc = any_other = False
res = sum("a" <= c <= "z" or "A" <= c <= "Z" for c in s)
print(res)
