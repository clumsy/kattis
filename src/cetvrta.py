p = [[int(i) for i in input().split()] for _ in range(3)]
p.sort()
if p[0][0] == p[1][0]:
    res = [p[2][0], p[0][1] + p[1][1] - p[2][1]]
else:
    res = [p[0][0], p[1][1] + p[2][1] - p[0][1]]
print(*res)
