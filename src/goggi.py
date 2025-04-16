s = input().split()
d = int(s[0]) - int(s[-1])
res = ">" if d > 0 else "<" if d < 0 else "Goggi svangur!"
print(res)
