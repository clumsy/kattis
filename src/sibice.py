from math import sqrt


n, w, h = (int(i) for i in input().split())
m = sqrt(w ** 2 + h ** 2)
for _ in range(n):
    i = int(input())
    res = "DA" if i <= m else "NE"
    print(res)
