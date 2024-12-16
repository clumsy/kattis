n = int(input())
res, g = None, -1
for _ in range(n):
    name, gift = input().split()
    gift = int(gift)
    if gift > g:
        res, g = name, gift
print(res)
