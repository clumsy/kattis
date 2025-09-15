n, a = int(input()), (int(i) for i in input().split())
mi1 = mi2 = float("inf")
for i in a:
    if i <= mi1:
        mi1, mi2 = i, mi1
    elif i < mi2:
        mi2 = i
res = mi1 + mi2
print(res)
