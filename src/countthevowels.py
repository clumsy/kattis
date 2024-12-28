s = input()
res = sum(c in "aeiou" for c in s.lower())
print(res)
