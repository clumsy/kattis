n = int(input())
a = input().split()
res, p = "makes sense", 0
for i in a:
    if i != "mumble":
        res = "something is fishy" if int(i) - p != 1 else res
    p += 1
print(res)
