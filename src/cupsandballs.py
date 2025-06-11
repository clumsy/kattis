h, n = int(input()), int(input())
x = 2
for _ in range(n):
    a, b = (int(i) for i in input().split())
    if a == x:
        x = b
    elif b == x:
        x = a
res = [h, x] if x != h else {1, 2, 3} - {h}
print(*res)
