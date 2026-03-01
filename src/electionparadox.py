n, a = int(input()), (int(i) for i in input().split())
res = 0
for i, e in enumerate(sorted(a)):
    res += e // 2 if i < ((n + 1) // 2) else e
print(res)
