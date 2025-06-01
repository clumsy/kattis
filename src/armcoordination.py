x, y = (int(i) for i in input().split())
r = int(input())
res = [(x - r, y + r), (x - r, y - r), (x + r, y - r), (x + r, y + r)]
for r in res:
    print(*r)
