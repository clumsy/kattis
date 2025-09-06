def rot(c, n):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    return s[(s.find(c) + n) % len(s)]
    
while True:
    s = input().split()
    if len(s) == 1:
        break
    n, s = int(s[0]), s[1]
    res = "".join(rot(c, n) for c in s[::-1])
    print(res)
