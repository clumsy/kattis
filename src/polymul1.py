t = int(input())
for _ in range(t):
    n1, a1 = int(input()) + 1, [int(i) for i in input().split()]
    n2, a2 = int(input()) + 1, [int(i) for i in input().split()]
    res = []
    for i1 in range(n1):
        for i2 in range(n2):
            k = i1 + i2
            while len(res) <= k:
                res.append(0)
            res[k] += a1[i1] * a2[i2]
    print(len(res) - 1)
    print(*res)
