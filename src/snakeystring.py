r, c = (int(i) for i in input().split())
res = [None] * c
for _ in range(r):
    s = input()
    for i, c in enumerate(s):
        if c != ".":
            res[i] = c
res = "".join(res)
print(res)
