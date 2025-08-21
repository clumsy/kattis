m = "qwertyuiopasdfghjklzxcvbnm"
n, s = int(input()), input()
res = "".join(m[ord(c) - ord("a")] if c != " " else " " for c in s)
print(res)
