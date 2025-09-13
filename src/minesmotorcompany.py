n = int(input())
x0 = y0 = None
res = 0
for _ in range(n):
    s = input()
    x, y = (ord(c) - ord("A") for c in s)
    if x0 is not None:
        res += abs(x - x0) + abs(y - y0)
    x0, y0 = x, y
print(res)
