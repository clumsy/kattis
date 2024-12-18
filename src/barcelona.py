n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
for i, e in enumerate(a):
    if e == k:
        res = i
        break
res = "fyrst" if i == 0 else "naestfyrst" if i == 1 else f"{i + 1} fyrst"
print(res)
