n = int(input())
for _ in range(n):
    a, b, c = (int(i) for i in input().split())
    res = "Possible" if (
       a - b == c or
       b - a == c or
       a + b == c or
       a * b == c or
       a == b * c or
       b == a * c
    ) else "Impossible"
    print(res)
