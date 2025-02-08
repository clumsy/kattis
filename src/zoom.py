from itertools import islice


n, k = (int(i) for i in input().split())
x = (int(i) for i in input().split())
res = islice(x, k - 1, (n // k) * k + 1, k)
print(*res)
