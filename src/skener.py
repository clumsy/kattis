r, c, zr, zc = (int(i) for i in input().split())
for _ in range(r):
    s = input()
    res = "".join(c * zc for c in s)
    for _ in range(zr):
        print(res)
