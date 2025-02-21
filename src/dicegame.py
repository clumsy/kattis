d = [0] * 2
for i in range(2):
    a1, b1, a2, b2 = (int(i) for i in input().split())
    d[i] = (b1 + a1) / 2 + (b2 + a2) / 2
res = "Gunnar" if d[0] > d[1] else "Emma" if d[0] < d[1] else "Tie"
print(res)
