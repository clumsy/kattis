n = int(input())
for _ in range(n):
    g = [int(i) for i in input().split()]
    for i in range(2, g[0]):
        if g[i + 1] - g[i - 1] == 1:
            res = i
    print(res)
