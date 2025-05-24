def mapc(c, m):
    o = (ord(c) - ord("A")) * int(m)
    return chr(ord("A") + o % 26)

def conv(s, m):
    res = "".join(mapc(ci, mi) for ci, mi in zip(s, m))
    return res

m, n = input(), int(input())
for _ in range(n):
    s = input()
    res = conv(s, m)
    print(res)
