t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res = (res * i) % 10
    print(res)
