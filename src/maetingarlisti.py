n, r, c = (int(i) for i in input().split())
rs = [input() for _ in range(r)]
for i in range(r):
    s = " ".join(input() for _ in range(c))
    res = "left" if rs[i] == s else "right"
    print(res)
