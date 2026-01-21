s = input()
res = chr(sum(ord(c) for c in s) // len(s))
print(res)
