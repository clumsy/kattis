n = int(input())
mi, res = float("inf"), -1
ds = (int(i) for i in input().split())
for i, d in enumerate(ds):
    if d < mi:
        mi, res = d, i
print(res)
