b = [1, 5, 15, 30, 150]
n = int(input())
res = []
while n:
    d, n = divmod(n, b.pop())
    res.append(d)
res += [0] * (5 - len(res))
res.reverse()
print(*res)
